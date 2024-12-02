# Escreva um programa que leia três números por parâmetro e mostre na tela em ordem crescente.

numeros = list()

for c in range(3):
    user = numeros.append(int(input()))
numeros.sort()
print("\n".join(str(c) for c in numeros))
