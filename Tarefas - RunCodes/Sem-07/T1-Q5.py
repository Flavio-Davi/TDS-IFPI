# Escreva um programa que leia três números inteiros correspondentes a três 
# notas de um aluno. Apresente a média das três notas, mas, se a terceira nota 
# for superior a 8, o aluno deve ganhar mais um ponto na média. Além disso, se
# a média final, em função do ponto extra, ficar acima de 10 ela deve ser ajustada para 10.

notas = list()
soma = 0

for c in range(3):
    nota = float(input())
    notas.append(nota)

for nota in notas:
    soma += nota

media = soma/3

if notas[2] > 8:
    media += 1

print(f"{media:.2f}" if media <= 10 else "10")
