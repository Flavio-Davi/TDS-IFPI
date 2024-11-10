# Escreva um programa que leia a idade de uma pessoa expressa em anos, meses 
# e dias e mostra na tela a idade dessa pessoa expressa apenas em dias. 
# Considerar sempre os anos com 365 dias e os meses com 30 dias.

anos = int(input())
meses = int(input())
dias = int(input())

IdadeDias = (anos*365) + (meses*30) + dias

print(IdadeDias)
