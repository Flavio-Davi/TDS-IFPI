# Faça um programa que pergunte ao usuário quantas fatias de pizza tem
# e quantos amigos vão dividir a pizza. Mostre quantas fatias cada um recebe e quantas sobram.

Fpizza = int(input("Quantas fatias, sua pizza tem?\n➥ "))
Apizza = int(input("\nÉ você e quantos amigos?\n➥ "))

print(f"Será {Fpizza//Apizza} fatias de pizza por pessoa :)!")
print(f"E assim sobrará {Fpizza%Apizza} fatia(s) de pizza")
