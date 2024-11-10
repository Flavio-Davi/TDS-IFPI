# Escreva um programa que leia a idade de uma pessoa expressa em anos, meses 
# e dias e mostra na tela a idade dessa pessoa expressa apenas em dias. 
# Considerar sempre os anos com 365 dias e os meses com 30 dias.

print(" DIAS NA TERRA ".center(45, "="))

print("\nDigite a baixo sua idade em anos, meses e dias para descobrir a quantos dias você está na terra.")
anos = int(input("\nAnos: "))
meses = int(input("Meses: "))
dias = int(input("Dias: "))

IdadeDias = (anos*365) + (meses*30) + dias

print(f"\nVocê está a {IdadeDias} dias na terra.")
