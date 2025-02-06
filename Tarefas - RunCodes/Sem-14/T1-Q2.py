# Usando apenas as estruturas básicas de programação, reescreva a funções count(), 
# que recebe uma lista e um valor e retorna o número de ocorrências do valor na lista. 
# Por exemplo count([1, 2, 3, 2, 4, 2, 5], 2) retorna 3, a quantidade de vezes que o 
# valor 2 aparece na lista.
# Faça a leitura pelo teclado, a leitura de um 0 (zero) encerra a leitura. Primeiro leia
# a lista e depois o valor para pesquisar. Imprima a lista que foi lida, o valor 
# pesquisado e o resultado encontrado.

def contar(dados, item):
    c = 0
    for i in dados:
        if i == item:
            c+=1
    return c


def main():
    user = None
    dados = []
    while user != 0:
        user = int(input())
        if user != 0:
            dados.append(user)

    pesquisa = int(input()) 
    print(dados)
    print(pesquisa)
    print(contar(dados, pesquisa))
    

if __name__ == '__main__':
    main()
