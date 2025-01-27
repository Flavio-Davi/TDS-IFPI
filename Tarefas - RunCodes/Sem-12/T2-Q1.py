# Escreva um programa que calcule o fatorial de um número inteiro lido, 
# sabendo-se que: N ! = 1 x 2 x 3 x ... x N-1 x N 0 ! = 1

from math import factorial

print(" CALCULO FATORAIL ".center(45, "#"))

user = int(input("\nDigite o número para calculo: "))
print(f"O fatorail de {user} é {factorial(user)}.")
