# Escreva um programa que leia três notas de um aluno, calcule e escreva 
# a média final deste aluno. Considerar que a média é ponderada e que o 
# peso das notas são 2, 3 e 5. Fórmula para o cálculo da média final é

print(" MÉDIA POR ALUNO ".center(45, "="))

n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))

media_ponderada = ((n1 * 2) + (n2 * 3) + (n3 * 5)) / 10

print(f"A média desse aluno é de {media_ponderada:.2f}")
