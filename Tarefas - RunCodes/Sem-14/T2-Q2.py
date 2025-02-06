# Escreva um programa que leia uma lista com 10 números reais, calcule e mostre a lista, 
# a quantidade de números negativos e a soma dos números positivos dessa lista.

dados = list()
negativos = 0
positivo = 0

for _ in range(10):
    dados.append(int(input()))

for i in dados: 
    if i<0:
        negativos+=1
    else:
        positivo+=i

print(dados)
print(negativos)
print(positivo)
