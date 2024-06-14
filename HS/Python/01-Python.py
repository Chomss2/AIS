#!/usr/bin/env python3
# -*- coding:utf-8 -*-
    #Endy T
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
def fReq() :
    req = requests.get
    url = "https://taisen.fr"
    res = req(url)
    print(res)


#IP et Nom du serveur DNS
def fDNS() :
    stream = os.popen('nslookup taisen.fr')
    output = stream.read().strip()
    print("IP et nom du serveur DNS : "+output)

#IP et Port Source et Destination
def fIPports() :
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("taisen.fr", 443))
    SourceDest = sock
    print("IP Source et Destination")
    print(sock.close)
    sock.close()

#Afficher les headers/leur utilité
def fHeaders() :
    html_content = res.text 
    soup = BeautifulSoup(html_content,"html.parser") 
    print("Liste des headers")
    print(soup)
    ##Array balises
    array = [tag.name for tag in soup.find_all()]
    # array = np.array(array)
    print("Tableau des headers")
    print(array)

##Elements du certificat
def fCert() :
    urlcert = "www.office.com"
    certbrut = ssl.get_server_certificate((urlcert, 443))
    cert = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, certbrut)
    print(cert.get_subject().get_components()) 

    #Chaine du certificat
    dlchaine = SSLCertificateChainDownloader()
    dlchaine.run({'host': urlcert})
    chaine = dlchaine.run({'host': urlcert})
    print(chaine)
#Liste des équipements
def fTracerout () : 
    hostname = "office.com"
    for i in range(1, 28):
        pkt = IP(dst=hostname, ttl=i) / TCP(dport=33434)
        # Send the packet and get a reply
        reply = sr1(pkt, verbose=0)
        if reply is None:
            # No reply =(
            print("Erreur")
            break
        elif reply.type == 3:
            # We've reached our destination
            print ("Done!", reply.src)
            break
        else:
            # We're in the middle somewhere'
          print ("%d hops away: " % i , reply.src)
####

if __name__ == "__main__" :

    #Requête
    fReq()
    #IP et Nom du serveur DNS
    fDNS()
    #IP source et destination
    fIPports()
    #Afficher les Headers et les balises
    req = requests.get
    url = "https://taisen.fr"
    res = req(url)
    fHeaders()
    #Afficher les informations du certificat et la chaine de confiance
    fCert()
    #Afficher les IP des équipements traversés 
    fTracerout()