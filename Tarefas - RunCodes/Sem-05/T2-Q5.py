# Escreva um programa que leia um caractere e mostra o valor booleano 
# True (verdadeiro) se for um SÍMBOLO (o que não é letra ou número) ou
# o valor booleano False (falso) caso contrário.

def valido(caracter):
    validar = "!@#$%¨&*()-_=+§´`[{]}º/?°~^ª<>.,|"

    if caracter in validar:
        return True
    else:
        return False


def main():
    print("-"*32)
    print("\tÉ letra/número?")
    print("-"*32)

    user = input("\nDigite um caracter: ").strip()[0]
    print(f"\nO caracter digitado é um síbolo:\n{valido(user)}")


if __name__ == "__main__":
    main()
