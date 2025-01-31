# Escreva um programa que ler a nota de 50 alunos. Mostre uma lista apenas com os 
# índices dos alunos que tem nota maior ou igual a 6 (seis).

notas = list()
for _ in range(5):
    notas.append(float(input()))

indic = list()

print([i for i in range(len(notas)) if notas[i]>=6])
