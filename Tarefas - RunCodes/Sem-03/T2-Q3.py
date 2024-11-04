# Escreva um programa que leia dois valores, um dividendo e um divisor. 
# Mostre o resultado da divisão e o resto da divisão inteira dos valores.

print(" CALCULADORA DE DIVVISÃO ".center(50, "@"))
v1 = float(input("\nValor 1: "))
v2 = float(input("Valor 1: "))

res = v1//v2
resD = v1%v2

print(f"Divisão inteira: {res:.4f}")
print(f"Resto da divisão: {resD:.4f}")
