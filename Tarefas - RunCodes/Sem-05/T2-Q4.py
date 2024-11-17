# Escreva um programa que leia um caractere e mostra o valor booleano True 
# (verdadeiro) se for uma letra (vogal ou consoante) ou um dígito (entre ‘0’ e ‘9’) 
# ou valor booleano False (falso) caso contrário.

def valido(caracter):
    alfabeto = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
    number = "0123456789"
    all = alfabeto + number

    if caracter in all:
        return True
    else:
        return False


def main():
    print("-"*32)
    print("\tÉ letra/número?")
    print("-"*32)

    user = input("Digite um caracter: ").strip()[0]
    print(f"\nO caracter digitado é uma letra ou númeral?\n{valido(user)}")


if __name__ == "__main__":
    main()
