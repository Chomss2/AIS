## Au début d'un script Python, on "import" des modules supplémentaires, ceux-ci sont téléchargés au préalable avec Powershell vont rajouter des "commandes"
## a notre script (ex : le module "OpenVPN" ajoute la commande "OpenVPN -Start" qui lance une connexion VPN")
import base64
#La syntaxe "From" = importer un module dans un module, ici, toutes ces sous catégories font partie du module "Cryptography"
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import secrets

## On va créer une fonction qui chiffre un message, avec 3 variables (cle, iv, message) 
def chiffre_message(cle, iv, message):
    #Il ne faut pas essayer de comprendre cette partie en profondeur, penchez vous-y une fois que vous avez compris le reste
    padder = padding.PKCS7(128).padder()
    message = message.encode()
    message = padder.update(message) + padder.finalize()
    cipher = Cipher(algorithms.AES(cle), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ct = encryptor.update(message) + encryptor.finalize()
    return ct

# Déchiffrer un message
#Même chose, on crée une commande qui déchiffre un message, avec 3 variable (clé, iv, message crypté)
def dechiffre_message(cle, iv, ct):
    #Même chose, inutile d'essayer de comprendre en profondeur ces commandes tant que vous ne comprenez pas le reste
    cipher = Cipher(algorithms.AES(cle), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    message = decryptor.update(ct) + decryptor.finalize()
    unpadder = padding.PKCS7(128).unpadder()
    message = unpadder.update(message) + unpadder.finalize()
    return message.decode()


## Ici, on a des variables qui s'utilisent en les citant (ex : keygen est une clé AES aléatoire)
keygen = secrets.token_bytes(32) # generation d'une cle AES aléatoire
ivgen = secrets.token_bytes(16) # generation d'IVs
#Pas besoin d'aborder celle-ci, le la commente

#
#Jusque ici, notre script ne fait donc RIEN, on a juste défini des fonctions et des variables,
#On viens de nous faire les outils, il faut maintenant les utiliser
#

#Pour chiffrer un message, il nous faudrait donc 3 éléments :
#Une clé (aléatoire), des IVs (aléatoire), et votre message

#Notre outil pour avoir une clé est "keygen", nous l'utilisons pour définir une variable "clé"
cléstatique = (keygen)

#Notre outil pour avoir des IV est "ivgen", nous l'utilisons pour définir une variable "iv"
ivstatique = (ivgen)

#On doit créér un message
messageclair = ("Salut la terre") 

#Et l'implémenter tout ca dans notre "Machine a chiffre des message"
#ATTENTION : On ajoute "print" avant notre machine, sinon, elle va faire l'opération, mais jamais nous dire le résultat
print (chiffre_message(cléstatique,ivstatique,messageclair))

#Cette commande est la SEULE renvoyée par notre script, sans "print" l'éxecution du script ne dira jamais rien
#Pareil, ici, on ne connait pas notre clé et iv, il faudrait les "print" pour ça (ex : print (cléstatique))

