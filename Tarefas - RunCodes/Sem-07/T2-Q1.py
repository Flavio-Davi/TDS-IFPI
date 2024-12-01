# Você sabia que os computadores amam contar coisas? Eles são como pequenos nerds! 
# Vamos fazer um contador de letras. Peça ao usuário para digitar uma frase qualquer 
# e, em seguida, imprima o número de caracteres nessa frase sem considerar espaços em 
# branco no início ou final da frase digitada.

def main():
    print(" Número de caracteres ".center(50, "="))
    user = input("\nDigite: ").strip().replace(" ", "")
    print(f"\nO número total de caracteres na frase/palavra é {len(user)}")


if __name__ == "__main__":
    main()
