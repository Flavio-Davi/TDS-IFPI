# Escreva um programa que leia uma temperatura em graus Celsius e mostra na 
# tela o valor correspondente em graus Fahrenheit

print(" CONVERSOR DE TEMPERATURA ".center(45, "="))
print("(Celsius para Fahrenheit)")
Celsius = float(input("\nDigite a temperatura em Celsius: "))

Fahrenheit = (Celsius * (9 / 5)) + 32

print(f"A temperatura {Celsius}° em Fahrenheit é de {Fahrenheit}°")
