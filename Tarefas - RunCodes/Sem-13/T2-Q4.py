# Escreva um programa que leia uma quantidade indeterminada de números reais, terminada 
# pela leitura de um número 0 (zero). O programa deve mostrar uma nova lista onde cada 
# elemento é a soma dos elementos anteriores da lista original. IMPORTANTE: Crie uma 2
# função chamada soma_cumulativa() que receba a lista original e retorna uma lista com 
# a soma cumulativa. Por exemplo:
# minha_lista = [1, 2, 3, 4, 5]
# somacumulativa(minhalista)
# [1, 3, 6, 10, 15]

def soma_cumulativa(lista):
    new_list = list()

    new_list.append(lista[0])
    for c in range(len(lista)):
        try:
            new_list.append(new_list[c]+lista[c+1])
        except:
            break    

    return new_list


def main():
    dados = list()
    print(" SOMA ACUMULATIVA ".center(30, "#"))
    while True:
        n = int(input("\nNúmmero (0 para parar): "))
        if n == 0:
            break
        dados.append(n)
    print(f"\nSoma acumulativa:\n{soma_cumulativa(dados)}")


if __name__ == '__main__':
    main()
