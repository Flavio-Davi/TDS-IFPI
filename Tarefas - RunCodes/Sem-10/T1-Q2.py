# Escreva um programa que leia o um 
# conjunto de 100 números inteiros 
# positivos e determine a quantidade 
# de números pares e números ímpares 
# contidos no mesmo


def testNumber(number):
    if number%2 == 0:
        return "PAR"
    else:
        return "IMPAR"


def main():
    pares = 0
    impares = 0

    for c in range(100):
        user = int(input())
        
        if testNumber(user) == "PAR":
            pares += 1
        else:
            impares += 1

    print(f"\n{pares} Par(es) digitado\n{impares} Ímpar(es) digitado")


if __name__ == "__main__":
    main()