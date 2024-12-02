# Escreva um programa que leia um número e mostra o valor booleano True (verdadeiro)
# se o número for ímpar ou o valor booleano False (falso) caso contrário

def par(num):
    return num%2 != 0


user = int(input())

print(par(user))
