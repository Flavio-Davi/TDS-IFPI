# Escreva um programa que leia uma quantidade n, seguido da leitura de uma lista 
# com n valores. O programa deve imprimir LISTA ORDENADA ou LISTA NÃO ORDENADA, 
# conforme o caso. IMPORTANTE: Crie uma função chamada esta_ordenado() que recebe 
# uma lista como parâmetro e retorne True se a lista estiver classificada em ordem 
# crescente, e False se não for o caso. Por exemplo:
# esta_ordenado([1, 2, 2]) True
# esta_ordenado(['b', 'a']) False

def esta_ordenado(lista):
    try:
        lista = [int(c) for c in lista]
        return True if lista == sorted(lista) else False
    except:
        return True if lista == sorted(lista) else False


def main():
    n = int(input().strip())
    lista_N = list()
    for _ in range(n):
        lista_N.append(input().strip())
    
    if esta_ordenado(lista_N):
        print("LISTA ORDENADA")
    else:
        print("LISTA NÃO ORDENADA")


if __name__ == '__main__':
    main()
