# Baseline Windows

## Question 

### 1️⃣ Utiliser auditpol pour l'authentification et les escalades de privilèges

``auditpol /set /category:"Connexion de compte" /failure:enable``

``auditpol /set /subcategory:"Ouvrir la session" /failure:enable``

### 2️⃣ Prouver la bonne configuration d'auditpol

![Copie d'écran de l'observateur d'évenements](Echec.png)

## Livrables 

### 1️⃣ Comparatif des LGPO / GPO

![Comparatif GPO Analyser](lgpo.png)

### 2️⃣ Résultat de la commande `Get-BitLockerVolume`

![Copie d'écran de l'output](Bitlocker.png)

### 3️⃣ Résultat de la commande `Get-MpPreference`

![Copie d'écran de l'output](defender.png)

### 4️⃣ Résultat de la commande `auditpol.exe /get /category:*`

![Copie d'écran de l'output](auditpol_answer.png)

### 5️⃣ Captures des logs avec échec d'authentification et escalade de privilèges

![Copie d'écran de l'observateur d'évenement](observateur.png)