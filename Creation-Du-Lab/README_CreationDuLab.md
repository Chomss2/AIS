# Création du Lab Dojo-101


## 1️⃣ Vérification de valeurs des hash 

Pour ce test, j'ai décidé de comparer mes hash avec une image de Debian 12.
Debian donnent leurs hashs sur une page dédiée sur leurs site, il nous suffit donc de vérifier l'authenticité du site sur lequel nous nous trouvons grace a son domaine.
Nous lançons en suite une commande `Get-FileHash` en spécifiant qu'il s'agit de SHA512, et nous comparons nos deux valeurs 

<p align="center">
    <img src="./Verification des hash.png" alt="Dojo-101" style="width: 500px;" />
</p>

## 2️⃣ Status des services DNS et et Web

Pour vérifier le fonctionnement de nos services web et DNS, nous lancons notre page web, et nous vérifions que le service DNS est bien disponible dans notre gestionnaire de serveur 


<p align="center">
    <img src="./Status DNS et Web.png" alt="Dojo-101" style="width: 500px;" />
</p>

## 3️⃣ Connexions WinRM et SSH

Pour vérifier nos connexions rien de plus simple, nous nous connectons
J'ai aussi vérifié l'accès par groupe sur linux en créant un utilisateur qui n'est pas dans le groupe requis, sa connexion est refusée

<p align="center">
    <img src="./Status SSH et WINRM.png" alt="Dojo-101" style="width: 500px;" />
</p>

## 4️⃣ Permissions et status des partages SMB

Pour vérifier nos permissions, nous pouvons utiliser le volet graphique "Sécurité" 


<p align="center">
    <img src="./Droits SMB.png" alt="Dojo-101" style="width: 500px;" />
</p>

## 5️⃣ Nombre d'utilisateur contenu dans l'AD

Pour vérifier notre nombre d'utilisateurs, nous utilisons la commande `(Get-AdUser -Filter * | Measure-Object).Count`

<p align="center">
    <img src="./Nombre d'utilisateurs dans l'AD.png" alt="Dojo-101" style="width: 500px;" />
</p>


Toutes nos informations sont bien vérifiés et notre infrastructure est fonctionnel ! 
