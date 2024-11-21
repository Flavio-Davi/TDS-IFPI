# Escreva um programa que leia um nome pelo teclado e informe quantos caracteres o nome possui.

def ContCarac(text):
    text = text.replace(" ", "")
    return len(text)


def main():
    print(" Contador de Caracteres ".center(45, "="))
    user = input("\nDigite: ").strip()
    print(f"\nO número total de caracteres na palavra/frase digitada é de {ContCarac(user)}.")

if __name__ == "__main__":
    main()  
