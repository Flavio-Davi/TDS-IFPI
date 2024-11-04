from tqdm import tqdm
from time import sleep
from os import system
# Desenvolva um programa que peça ao usuário o nível de volume atual 
# e o nível de volume desejado de seu aparelho de som. Calcule e mostre a diferença de volume necessária.

VolAtu = int(input("Digite o volume atual: "))
VolDes = int(input("Digite o volume desejado: "))

dif = (VolAtu-VolDes)*-1

conf = input(f"\nA diferença do volume atual para o desejado é de {dif}, confirmar alteração\n [ 1 ] - SIM\n [ 2 ] - Não\n➥ ")

if conf == "1" or "SIM":
    system("cls")
    for c in tqdm(range(0, 100)):
        sleep(0.05)
    print(f"Volume alterado para {VolDes}")
else:
    print("\nTudo bem, caso queira alterar me deixo a disposição! :)")
    