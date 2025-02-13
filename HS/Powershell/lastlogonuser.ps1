# Get current date and hostname for the report filename
$date = Get-Date -Format "yyyy-MM-dd"
$hostname = $env:COMPUTERNAME
$outputPath = "LastLogons_${hostname}_$date.csv"

# Get domain information
$domain = [System.DirectoryServices.ActiveDirectory.Domain]::GetCurrentDomain()
$domainPath = "LDAP://" + $domain.Name

# Get all user profiles from the registry
$profiles = Get-WmiObject -Class Win32_UserProfile | 
    Where-Object { -not $_.Special } |
    Select-Object LocalPath, LastUseTime

# Create an array to store the results
$results = @()

foreach ($profile in $profiles) {
    try {
        # Extract username from profile path
        $username = $profile.LocalPath.Split('\')[-1]
        
        # Convert LastUseTime to readable format
        $lastUse = if ($profile.LastUseTime) {
            [System.Management.ManagementDateTimeConverter]::ToDateTime($profile.LastUseTime)
        } else {
            "Never logged on"
        }
        
        # Check if user account is enabled using ADSI
        $isEnabled = "Unknown"
        try {
            $searcher = New-Object System.DirectoryServices.DirectorySearcher
            $searcher.SearchRoot = New-Object System.DirectoryServices.DirectoryEntry($domainPath)
            $searcher.Filter = "(&(objectCategory=person)(objectClass=user)(sAMAccountName=$username))"
            $user = $searcher.FindOne()
            
            if ($user) {
                # UAC (UserAccountControl) flag for disabled accounts is 0x2
                $uac = $user.Properties["useraccountcontrol"][0]
                $isEnabled = -not [bool]($uac -band 0x2)
            }
        } catch {
            # If AD check fails, leave as "Unknown"
        }
        
        # Create custom object with profile information
        $profileInfo = [PSCustomObject]@{
            ServerName = $hostname
            Username = $username
            IsEnabled = $isEnabled
            LastLogon = $lastUse
            ProfilePath = $profile.LocalPath
        }
        
        $results += $profileInfo
    }
    catch {
        Write-Warning "Error processing profile for $username"
    }
}

# Export results to CSV
$results | Export-Csv -Path $outputPath -NoTypeInformation

# Display results in console
$results | Format-Table -AutoSize

Write-Host "`nReport exported to: $outputPath"