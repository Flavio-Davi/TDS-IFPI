# Escreva um programa que leia um número inteiro positivo e escreva na tela:
# • FIZZ se o número é divisível por três;
# • BUZZ se o número é divisível por cinco;
# • FIZZBUZZ se o número é divisível por três e por cinco ao mesmo tempo.
# • O próprio número caso não seja divisível por três ou por cinco.
# OBS: para cada número lido apenas uma resposta deve ser impressa.

def text(num):
    if num%5 == 0 and num%3 == 0:
        return "FIZZBUZZ"
    elif num%3 == 0:
        return "FIZZ"
    elif num%5 == 0:
        return "BUZZ"
    else:
        return num


def main():
    print(" FIZZ ou BUZZ ".center(44, "@"))
    print("""\n• FIZZ se o número é divisível por três;
• BUZZ se o número é divisível por cinco;
• FIZZBUZZ se o número é divisível por três e por cinco ao mesmo tempo.
• O próprio número caso não seja divisível por três ou por cinco.""")

    num = int(input("\nDigite um número inteiro posivito: "))
    print(f">>> {text(num)}")


if __name__ == "__main__":
    main()