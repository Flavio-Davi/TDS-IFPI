# Escreva um programa que leia um caractere e mostra o valor booleano 
# True (verdadeiro) se for uma letra (vogal ou consoante) ou o valor 
# booleano False (falso) caso contrário.

def validar(caracter):
    vogal = "AaEeIiOoUu"
    consoante = "BbCcDdFfGgHhJjKkLlMmNnPpQqRrSsTtVvWwXxYyZz"
    all = vogal+consoante

    if caracter in all:
        return True
    else:
        return False


def main():
    print("-"*25)
    print("\tÉ letra?")
    print("-"*25)

    user = input("\nDigite um caracter: ").strip()[0]
    print(f"\nO caracter digitado é letra?\n{validar(user)}")

if __name__ == "__main__":
    main()
