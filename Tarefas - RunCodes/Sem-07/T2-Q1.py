# Escreva um programa que leia o nome e o estado civil de uma pessoa, 
# considere apenas “1” para casado e “2” para solteiro. Se a pessoa for casada, 
# leia, também, o nome do cônjuge. Mostre quantos caracteres no total existem no(s) nome(s) lido(s).

nome = input().strip().replace(" ", "")
est_civil = input().strip()

if est_civil == "1":
    conjugue = input().strip().replace(" ", "")
    print(len(nome)+len(conjugue))
else:
    print(len(nome))
