# Escreva um programa que leia um valor inteiro e mostra na tela no valor 
# booleano True caso o número lido seja maior que 100 ou False caso contrário.

print("Digite a baixo um número, se superior a 100 o valor será True(Verdadeiro), se não será False(False)")

valor = int(input("\nValor: "))

print(f"O valor digitado é {True if valor>100 else False}.")
