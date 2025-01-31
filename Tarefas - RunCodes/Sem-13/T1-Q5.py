# Leia duas listas A e B contendo 25 elementos inteiros cada, gerar e imprimir 
# uma lista C de 50 elementos, cujos elementos sejam a intercalação dos elementos de A e B.

def main():
    lista_A = list()
    lista_B = list()
    lista_C = list()

    print(" LISTAS INTERCALADAS ".center(40, "#"))
    for c in range(25):
        lista_A.append(int(input(f"Lista A[{c}/25]: ")))
    for c in range(25):
        lista_B.append(int(input(f"Lista B[{c}/25]: ")))
    for dado in zip(lista_A, lista_B):
        for item in dado:
            lista_C.append(item)

    print(f"Lista A: {lista_A}")
    print(f"Lista B: {lista_B}")
    print(f"Lista C: {lista_C}")
    

if __name__ == '__main__':
    main()
