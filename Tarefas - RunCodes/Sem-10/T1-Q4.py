# Escreva um programa que gere a seguinte sequência: 10, 20, 30, 40, ..., 990, 1000. 
# Considere a separação dos números por vírgula seguido de espaço em brando e o pontos no final da sequência.
from time import sleep
cont = 0

print(" CONTADOR - de 10 em 10 ".center(25, "#"))
try:
    user = int(input("Digite até quanto você quer o contador\n-> "))
except:
    print("ERROR: Entrada inválida.")
    sleep(1)
    user = int(input("Digite até quanto você quer o contador\n(Apenas números inteiro)\n-> "))

while cont < user:
    cont += 10
    if cont == 1000:
        print(f"{cont}.")
    else:
        print(cont, end=", ", flush=True)
        sleep(0.05)
        