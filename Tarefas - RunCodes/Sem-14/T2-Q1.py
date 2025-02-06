# Escreva um programa que leia 10 números inteiros e os armazene em uma lista. 
# Imprima a lista, o maior elemento e a posição que ele se encontra.

dados = list()
for _ in range(10):
    dados.append(int(input()))

print(dados)
print(max(dados))
print(dados.index(max(dados)))
