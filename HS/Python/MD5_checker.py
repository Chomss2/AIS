import hashlib
import sys

def calculate_md5(text):
    """Calculate MD5 hash of given text."""
    return hashlib.md5(text.encode('utf-8')).hexdigest()

def check_hash_against_wordlist(target_hash, wordlist_path):
    """
    Check if any word in the wordlist matches the target hash when converted to MD5.
    Returns the matching word if found, None otherwise.
    """
    try:
        with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as file:
            for line in file:
                word = line.strip()
                if not word:  # Skip empty lines
                    continue
                    
                current_hash = calculate_md5(word)
                if current_hash == target_hash:
                    return word
        return None
        
    except FileNotFoundError:
        print(f"Error: Wordlist file '{wordlist_path}' not found.")
        sys.exit(1)
    except PermissionError:
        print(f"Error: Permission denied accessing '{wordlist_path}'.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading wordlist: {str(e)}")
        sys.exit(1)

def main():
    # Get target hash from user
    target_hash = input("Enter the MD5 hash to find: ").strip().lower()
    
    # Validate hash format (MD5 hashes are 32 characters long)
    if len(target_hash) != 32 or not all(c in '0123456789abcdef' for c in target_hash):
        print("Error: Invalid MD5 hash format. Please enter a 32-character hexadecimal hash.")
        sys.exit(1)
    
    # Get wordlist path from user
    wordlist_path = input("Enter the path to the wordlist file: ").strip()
    
    print("\nSearching...")
    
    # Check wordlist for matching hash
    result = check_hash_against_wordlist(target_hash, wordlist_path)
    
    if result:
        print(f"\nMatch found!")
        print(f"Hash: {target_hash}")
        print(f"Original text: {result}")
    else:
        print("\nNo match found in the wordlist.")

if __name__ == "__main__":
    main()