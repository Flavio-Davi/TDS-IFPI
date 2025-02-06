# Foram anotados nomes, idades e alturas de 30 alunos. Faça um programa 
# que determine quais alunos com mais de 13 anos possuem altura inferior à 
# média de altura dos alunos.

def analise(nomes, idade, altura):
    dados = []

    mediaAltura = round(sum(altura)/len(altura), 2)

    for c in range(len(idade)):
        if idade[c]>13 and altura[c]<mediaAltura:
            dados.append(nomes[c])

    return dados            
    

def main():
    dadosNome = []
    dadosIdade = []
    dadosAltura = []

    for c in range(3):
        dadosNome.append(input())
        dadosIdade.append(int(input()))
        dadosAltura.append(float(input()))

    print(f"MAIORES DE 13 ANOS COM ALTURA ABAIXO DA MÉDIA")
    print("\n".join(map(str, [d for d in analise(dadosNome, dadosIdade, dadosAltura)])))


if __name__ == '__main__':
    main()
