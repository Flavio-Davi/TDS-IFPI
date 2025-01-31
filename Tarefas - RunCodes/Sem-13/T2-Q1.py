# Escreva um programa que leia uma quantidade indeterminada de números inteiros, 
# terminada pela leitura de um número 0 (zero). Depois, leia um valor inteiro constante. 
# O programa deve mostrar uma nova lista onde cada valor da lista original é a 
# multiplicado pelo valor da constante.
# IMPORTANTE: Crie uma função chamada multiplica_constante() que receba a lista original e o 
# valor da constante e retorna uma nova lista com os elementos multiplicados.

def multiplica_constante(lista, constante):
    new_list = list()
    for dado in lista:
        new_list.append(dado*constante)
    
    return new_list


def main():    
    dados = list()
    print(" Multiplicação de lista ".center(50, "@"))
    while True:
        n = int(input("\nNúmero (0 para parar): "))
        if n == 0:
            break
        dados.append(n)
        
    VALOR = int(input("\nN° que será multiplicado: "))
    print(f"\nNúmeros multplicado pela constante {VALOR}:\n{multiplica_constante(dados, VALOR)}")


if __name__ == '__main__':
    main()
