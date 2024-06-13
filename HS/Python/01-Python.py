#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#Modules
import requests
import urllib
import dns.resolver
import socket
from bs4 import BeautifulSoup
import ssl
import OpenSSL
import numpy as np
from get_certificate_chain.download import SSLCertificateChainDownloader
from scapy.all import *
#Variables Request
req = requests.get
url = "https://taisen.fr"
res = req(url)

#IP et Nom du serveur DNS
stream = os.popen('nslookup taisen.fr')
output = stream.read().strip()

#IP et Port Source et Destination
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect(("taisen.fr", 443))
SourceDest = socket
print(socket.close)
socket.close()

#Afficher les headers/leur utilité
html_content = res.text 
soup = BeautifulSoup(html_content,"html.parser") 

##Array balises
array = [tag.name for tag in soup.find_all()]
array = np.array(array)

##Elements du certificat
urlcert = "www.office.com"
certbrut = ssl.get_server_certificate((urlcert, 443))
cert = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, certbrut)
cert.get_subject().get_components() 
#Chaine du certificat
dlchaine = SSLCertificateChainDownloader()
dlchaine.run({'host': urlcert})
chaine = dlchaine.run({'host': urlcert})
#Liste des équipements 
hostname = "taisen.fr"
for i in range(1, 28):
    pkt = IP(dst=hostname, ttl=i) / TCP(dport=33434)
    # Send the packet and get a reply
    reply = sr1(pkt, verbose=0)
    if reply is None:
        # No reply =(
        break
    elif reply.type == 3:
        # We've reached our destination
        print ("Done!", reply.src)
        break
    else:
        # We're in the middle somewhere'
        print ("%d hops away: " % i , reply.src)