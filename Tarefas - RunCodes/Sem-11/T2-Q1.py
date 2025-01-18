# Escreva um programa que leia um conjunto de números inteiros e exiba a soma dos mesmos. Observação:
# A condição de saída do laço será a leitura do valor 0 (flag).

def main():
    print(" SOMA ".center(30, "@"))
    user = None
    sum = 0
    while user != 0:
        user = int(input("Número: "))
        sum += user
    print(f"A soma dos números é {sum}")


if __name__ == "__main__":
    main()
