from os import system
from time import sleep
# Você encontrou uma varinha mágica que pode dobrar qualquer coisa! 
# Mas espere... Isso funcionaria com números? Vamos tentar! Peça ao 
# usuário para inserir um número. Em seguida, calcule o dobro desse número e imprima o resultado.

def carregando(x):
    for c in range(0, x):
        system("cls")
        print("Fazendo a mágia/.")
        sleep(0.5)
        system("cls")
        print("Fazendo a mágia\.")
        system("cls")
        sleep(0.5)
        

cores = {red:="\033[1;31m", green:="\033[1;32m", yeloow:="\033[1;33m"}
num = float(input("Digite um número: "))

dobro = num*2
carregando(4)
print(f"🪄 {dobro}")
