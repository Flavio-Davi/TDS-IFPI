# Calcular H = 1 + 1/2 + 1/3 + 1/4 + ... + 1/n, escreva um programa para calcular o 
# valor de H com 4 (quatro) casas decimais. O número n é lido.

def calcular(x):
    total = 0.0

    for c in range(1, x+1):
        total += 1.0/c

    return total


def main():
    print(" SOMA, SEQ(1/2, 1/3/ 1/4... 1/N) ".center(50, "#"))
    user = int(input("\nN: "))
    print(f"\nA soma da sequência é {calcular(user):.4f}")


if __name__ == "__main__":
    main()
