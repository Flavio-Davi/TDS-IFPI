# Escreva um programa que leia um número inteiro entre 100 e 999, 
# mostre quantos dígitos pares existem nesse número. Por exemplo: 
# 245 tem 2 dígitos pares; 135 tem 0 dígitos pares; 134 tem 1 dígito par.

def par(x):
    return x%2 == 0


def main():
    user = input()
    cont_par = 0

    for c in user:
        if par(int(c)):
            cont_par += 1

    print(cont_par)


if __name__ == "__main__":
    main()
