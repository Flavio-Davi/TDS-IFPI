# Escreva um programa que leia um único caractere pelo teclado e 
# informe o código numérico correspondente ao caractere lido.

def main():
    print(" Código Unicode por caracter ".center(45, "="))
    print("\nDigite UM caracter a baixo para saber o código unicode\n(Caso digite mais de um caracter, apenas o primeiro será considerado)")
    
    user = input("\nDigite: ")[0]
    print(f"O código unicode de, {user}, é {ord(user)}.")

if __name__ == "__main__":
    main()
