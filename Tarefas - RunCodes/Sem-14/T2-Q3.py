# Escreva um programa que leia uma lista com 20 números inteiros. Escreva os 
# elementos da lista eliminando elementos repetidos.

def repetidos(x):
    end_dados = list()
    
    for c in x:
        if c not in end_dados:
            end_dados.append(c)
    
    return end_dados


def main():
    dados = list()
    for c in range(20):
        dados.append(int(input()))

    print(repetidos(dados))


if __name__ == '__main__':
    main()
