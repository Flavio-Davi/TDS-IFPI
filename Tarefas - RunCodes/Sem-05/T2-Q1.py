# Escreva um programa que leia um caractere e mostra o valor booleano 
# True (verdadeiro) se for uma vogal ou o valor booleano False (falso) caso contrário.

def vogal(caracter):
    vogal = "AaEeIiOoUu"
    for c in range(len(vogal)):
        if caracter == vogal[c]:
            return True
    return False


def main():
    print("-"*25)
    print("\tÉ vogal?")
    print("-"*25)

    user = input("\nDigite um caracter: ").strip()[0]
    print(f"\nO caracter digita é vogal?\n{vogal(user)}")

if __name__ == "__main__":
    main()
