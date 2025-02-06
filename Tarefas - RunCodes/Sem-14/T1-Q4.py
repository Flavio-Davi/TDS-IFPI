# Um time de basquete possui 12 jogadores. Deseja-se um programa que, dado o 
# nome e a altura dos jogadores, determine: a. o nome e a altura do jogador mais alto; 
# b. a média de altura do time; c. os jogadores com altura superior à média, listando 
# o nome e a altura de cada um.
def A(dados):
    nomes = list()
    altura = list()

    for c in range(len(dados)):
        if c%2==0:
            nomes.append(dados[c])
        else: altura.append(float(dados[c].strip()))

    maisAltoNome = nomes[altura.index(max(altura))]
    maisAlto = max(altura)
    fim = f"{maisAltoNome}\n{maisAlto:.2f}"

    return fim


def B(dados):
    altura = list()

    for c in range(len(dados)):
        if c%2 != 0:
            altura.append(float(dados[c].strip()))

    mediaAltura = sum(altura)/len(altura)
    return mediaAltura


def C(dados):
    nomes = list()
    altura = list()

    for c in range(len(dados)):
        if c%2==0:
            nomes.append(dados[c])
        else: altura.append(float(dados[c].strip()))

    mediaAltura = sum(altura)/len(altura)
    supMedia = []

    for c in range(len(altura)):
        if altura[c] > mediaAltura:
            supMedia.append(nomes[c])
            supMedia.append(f"{altura[c]:.2f}")

    return supMedia


def main():
    dados = []
    for c in range(24):
        dados.append(input())

    print("JOGADOR MAIS ALTO DO TIME")
    print(f"{A(dados)}")
    print("ALTURA MÉDIA DO TIME")
    print(f"{B(dados):.2f}")
    print("JOGADORES MAIS ALTOS QUE A MÉDIA DO TIME")
    for i in C(dados):
        print(i)

if __name__ == main():
    main()