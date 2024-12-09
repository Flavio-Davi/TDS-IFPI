# Escreva um programa que leia um número inteiro. Mostre a soma dos dígitos para os 
# números entre 0 (zero) e 100 mil ou -1 para outros valores. Por exemplo: Em 16.759
# a soma dos dígitos é 1 + 6 + 7 + 5 + 9 = 31 é o valor retornado; Em 136.759 o valor
#  lido é maior que 100 mil e deve retornar -1; Em -100 o valor lido é negativo e deve retornar -1.

def sum_all(num):
    ind = str(num)
    total = 0
    if 100000 > num > 0:
        for c in range(len(ind)):
            total += int(ind[c])
    else:
        total = -1
    return total


def main():
    print(" SOMA DOS DÍGITOS ".center(44, "#"))
    num = int(input("\nDigite um número: "))
    print(f"\nA soma dos dígitos {num} é {sum_all(num)}")


if __name__ == "__main__":
    main()
