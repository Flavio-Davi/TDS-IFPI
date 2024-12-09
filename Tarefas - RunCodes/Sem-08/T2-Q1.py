# Escreva um programa que leia um número inteiro e some 5 caso valor lido seja 
# par ou some 8 caso o valor lido seja ímpar. Mostre na tela o resultado da operação.

def soma_se(x):
    if x%2 == 0:
        x += 5
    else:
        x += 8
    return x


def main():
    print(" Par soma 5, Ímpar soma 8".center(44, "@"))
    num = int(input("Digite um número inteiro: "))
    print(f"\n>>> {soma_se(num)}")


if __name__ == "__main__":
    main()
