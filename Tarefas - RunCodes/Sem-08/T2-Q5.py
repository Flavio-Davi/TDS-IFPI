# Escreva um programa que leia o número de matrícula de um aluno, suas notas em 3
# provas e a média das notas obtidas nos exercícios que fazem parte da sua avaliação. 
# Calcule a média final usando a fórmula:
# Média Final = (Nota 1 + Nota 2 * 2 + Nota 3 * 3 + Média Exercícios) / 7
# A atribuição dos conceitos obedece a tabela abaixo. 
# A	>= 9.0
# B	>= 7.5 e < 9.0
# C	>= 6.0 e < 7.5
# D	>= 4.0 e < 6.0
# E	< 4.0
# O programa deve escrever a matrícula do aluno, a média final, o conceito correspondente
# e a mensagem “Aprovado” se o conceito for A, B ou C ou “Reprovado” se o conceito for D ou E.
# Aprovado  ->	A, B ou C
# Reprovado ->	D ou E

def media_fim(notas, med_ex):
    conceito = (notas[0] + notas[1] * 2 + notas[2] * 3 + med_ex) / 7
    mediaFim =  f"{conceito:.2f}"
    
    if conceito >= 9:
        conceito = "A"
    elif  7.5 <= conceito < 9:
        conceito = "B"
    elif 7.5 > conceito >= 6:
        conceito = "C"
    elif 6 > conceito >= 4:
        conceito = "D"
    else:
        conceito = "E"
    
    if conceito == "A" or conceito == "B" or conceito == "C":
        return [mediaFim, conceito, "Aprovado"]
    else:
        return [mediaFim, conceito, "Reprovado"]


def main():
    print(" BOLETIM ".center(44, "="))
    matricula = input("\nDigite sua matrícula: ")
    notas = list()
    for c in range(1, 4):
        notas.append(float(input(f"{c}° nota: ")))
    media_ex = float(input("Média de exercícios: "))
    
    dados = media_fim(notas, media_ex)
    print(f"\nMatrícula: {matricula}")
    print(f"Média final: {dados[0]}\nConceito: {dados[1]}\nSituação: {dados[2]}")
    


if __name__ == "__main__":
    main()
