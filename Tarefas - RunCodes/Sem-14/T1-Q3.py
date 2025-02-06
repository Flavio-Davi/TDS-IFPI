# Dadas duas listas A e B contendo 20 elementos inteiros cada, gerar e exibir uma 
# lista C do mesmo tamanho cujos elementos sejam a soma dos respectivos elementos de A e B.

def soma_lista(dadosA, dadosB):
    soma_all = []
    for a, b in zip(dadosA, dadosB):
        soma_all.append(a+b)
    return soma_all


def main():
    lista_A = []
    lista_B = []

    for _ in range(20):
        lista_A.append(int(input()))
    for _ in range(20):
        lista_B.append(int(input()))

    print(lista_A)
    print(lista_B)
    print(soma_lista(lista_A, lista_B))


if __name__ == '__main__':
    main()
