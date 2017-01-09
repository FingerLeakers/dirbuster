import requests
import sys
from os import system

def Plataforma():
    if sys.platform != "linux2":
        system("cls")
    else:
        system("clear")
                           
def Banner():
    print """

  _____           _ _      
 |  __ \         | (_)     
 | |__) |   _  __| |_ _ __ 
 |  ___/ | | |/ _` | | '__|
 | |   | |_| | (_| | | |   
 |_|    \__, |\__,_|_|_|   
         __/ |             
        |___/              

[+]Github:   github.com/nash0x27
[+]Email:    gabrieldutra-08@protonmail.com
[+]Facebook: fb.com/n4shxx

=============================================
Uso:
    Alvo: site.com.br

=============================================
"""                                           
                                            
def Main():
    wordlist1 = open('wordlist/wordlist.txt')
    diretorios = wordlist1.readlines()
    
    alvo = raw_input("Alvo: ")
    url = 'http://'+alvo+'/'

    for diretorio in diretorios:
        error = 404

        if diretorio[0] != "#":
            resposta = requests.get(url+diretorio)
            error = resposta.status_code

        if diretorio != 404:
            print url+diretorio, error
Plataforma()
Banner()
Main()
