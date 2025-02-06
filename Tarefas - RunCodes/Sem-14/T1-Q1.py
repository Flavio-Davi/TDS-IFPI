# As estruturas básicas de programação são sequência, condição e repetição. Usando apenas as 
# estruturas básicas de programação, reescreva as funções abaixo (sem utilizá-las):
# a) len(), que recebe uma lista e retorna número de itens; 
# b) reverse(), que recebe uma lista e retorna uma lista com os itens na ordem invertida; 
# c) min(),que recebe uma lista e retorna o menor valor 
# d) max(), que recebe uma lista retorna o maior valor 
# e) sum(), que recebe uma lista retorna a soma dos valores
# Faça a leitura dos valores necessários pelo teclado, a leitura de um número 0 (zero) 
# encerra a leitura dos elementos da lista. Para cada uma das opções, imprima a
#  lista que foi lida e o resultado encontrado.
# Dica: Você pode usar esses nomes para suas funções: comprimento(), inverter(), minimo(), maximo(), soma().


def contar(x):
    t = 0
    for i in x:
        t+=1
    return t


def rever(x):
    return x[::-1]


def minimo(x):
    menor = x[0]
    temp = x.copy()

    for c in x:
        for i in temp:
            if c < i and c < menor:
                menor = c            
    return menor


def maior(x):
    m = 0
    for i in x:
        if i > m:
            m = i
    return m


def soma(x):
    s = 0
    for c in x:
        s += c
    return s


def main():
    user = None
    list_user = list()

    while user != 0:
        user = int(input())
        if user != 0:
            list_user.append(user)

    print(list_user)
    print(contar(list_user))
    print(rever(list_user))
    print(minimo(list_user))
    print(maior(list_user))
    print(soma(list_user))

if __name__ == '__main__':
    main()
