# Escreva um programa que leia um caractere e mostra o valor booleano 
# True (verdadeiro) se for uma consoante ou o valor booleano False (falso) caso contrário.

def validar(caracter):
    consoante = "BbCcDdFfGgHhJjKkLlMmNnPpQqRrSsTtVvWwXxYyZz"

    if caracter in consoante:
        return True
    else:
        return False


def main():
    print("-"*28)
    print("\tÉ consoante?")
    print("-"*28)

    user = input("\nDigite um caracter: ").strip()[0]
    print(f"\nO caracter digitado é uma cosoante?\n{validar(user)}")


if __name__ == "__main__":
    main()
