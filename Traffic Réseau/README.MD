# Traffic Réseau, Wireshark

## 1️⃣ Rappels

* **Quelle est votre adresse IP, quel est sa classe ?**

    Mon adresse ip est 192.168.0.45, c'est une ip de classe C

* **Quel est votre masque de sous réseau**

    Mon masque de sous réseau est /24, ou 255.255.255.0

* **Quel est l'adresse de votre passerelle**

    Ma passerelle est en 192.168.0.1
## 2️⃣ Questions

### 1️⃣ Quels sont les flags TCP

* Les flags sont des bit contenus dans l'entête qui donnent une information sur la nature du paquet

* URG indique que le champ Pointeur de donnée urgente est utilisé.
* ACK indique que le numéro de séquence pour les acquittements est valide.
* PSH indique au récepteur de délivrer les données à l’application  et de ne pas attendre le remplissage des tampons.
* RST demande la réinitialisation de la connexion.
* SYN indique la synchronisation des numéros de séquence.
* FIN indique fin de transmission.

### 2️⃣ Capturer le processus DORA du DHCP

![alt text](DORA_DHCP.png "Capture DORA")

### 3️⃣ DHCP Starvation / DHCP snooping / Rogue DHCP 

* Une attaque DHCP Starvation est une attaque de type DoS qui vise a flooder le serveur DHCP de requêtes pour qu'il ai attribué toutes ses adresse disponible, et ainsi bloquer son fonctionnement
* Le DHCP Snooping est une fonctionnalité de couche 2 qui va bloquer les Offres DHCP venant d'une source suspecte et triant ses ports
* Un Rogue DHCP est un serveur DHCP qui n'a pas été installé par l'équipe infrastructure, par des raisons d'innatentions ou de malveillance

