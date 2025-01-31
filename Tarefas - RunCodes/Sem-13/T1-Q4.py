# Leia 20 números inteiros e armazene-os numa lista. Armazene os números pares na lista
# PAR e os números ímpares na lista IMPAR. Imprima as três listas

def main():
    par = list()
    impar = list()
    all = list()
    
    for c in range(1, 21):
        user = int(input(f"Digite[{c}/20]: "))
        all.append(user)
        if user%2 == 0: 
            par.append(user) 
        else: 
            impar.append(user)

    print(f"\nTODOS: {all}\nPARES: {par}\nIMPARES: {impar}")


if __name__ == '__main__':
    main()
