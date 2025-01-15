# Escreva um programa que leia um conjunto de números inteiros e exiba a soma dos mesmos. Observação:
# A condição de saída do laço será a leitura do valor 0 (flag).

def main():
    user = int(input())
    sum = 0
    while user != 0:
        sum += user
        user = int(input())
    print(sum)


if __name__ == "__main__":
    main()
