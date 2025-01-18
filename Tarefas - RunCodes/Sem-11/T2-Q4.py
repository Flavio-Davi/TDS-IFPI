# O cardápio de uma casa de lanches, especializada em sanduíches, é dado abaixo.
# CÓDIGO  PRODUTO         PREÇO (R$)
# H       Hamburger       5.50
# C       Cheeseburger    6.80
# M       Misto Quente    4.50
# A       Americano       7.00
# Q       Queijo Prato    4.00
# X       PARA TOTAL DA CONTA
# Escreva um programa que leia o código e a quantidade de cada item comprado por um
# freguês, calcule e exiba o total a pagar. Obs: A leitura do código 'X' indica o fim dos itens.
from os import system
import platform
from time import sleep

class cardapio():
    def __init__(self):
        self.opc = {"H": ["Hamburger", 5.50],
               "C": ["Cheeseburger", 6.8],
               "M": ["Misto Quente", 4.50],
               "A": ["Americano", 7.00],
               "Q": ["Queijo Prato", 4.00]}
        self.color()
        self.user()
        

    def limpar_tela(self):
        if platform.system() == "Windows": 
            system("cls") 
        else: 
            system("clear")


    def color(self):
        self.cores = {"red": "\033[1;31m", "green": "\033[1;32m", 
                      "yellow": "\033[1;33m", "blue": "\033[1;34m",
                      "pink": "\033[1;35m", "cyan": "\033[1;36m",}


    def showMenu(self):
        print(self.cores["cyan"]+" CARDÁPIO ".center(50, "#"))
        print(self.cores["yellow"]+f"\n{'CÓDIGO':<10} {'ITENS':<20} {'PREÇO (R$)':>10}")
        for key, value in self.opc.items():
            print(f"{key:<10} {value[0]:<20} {value[1]:>10}")


    def  user(self):
        user = None
        self.total = 0
        
        while user != "X":
            self.limpar_tela()
            self.showMenu()
            print(self.cores["green"]+f"{'X':<10} {'PARA TOTAL DA CONTA':<20} {self.total:>10}")
            user = input(self.cores["cyan"]+"\nCódigo: ").upper()
            
            if user != "X":
                try:
                    self.total += self.opc[user][1]           
                    print(self.cores["green"]+">>> ADICIONADO")
                    sleep(1)
                except:
                    print(self.cores["red"]+"ERROR: OPÇÃO INVÁLIDA")
                    sleep(1)
            else:
                print(f"TOTAL R${self.total}")
                break

cardapio()
