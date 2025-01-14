# Escreva um programa que leia uma quantidade indefinida de números inteiros 
# positivos terminada pelo número 0 (zero). Ao final, o programa deve mostrar 
# a média aritmética de todos os números lidos (excluindo o zero).

def main():
    print(" MÉDIA ARITIMÉTICA ".center(60, "="))

    numeros = list()
    user = int(input("Digite: "))
    numeros.append(user)
    
    while user != 0:
        user = int(input("Digite: "))
        numeros.append(user)
    
    numeros.remove(0)
    soma = 0
    for c in range(len(numeros)):
        soma += numeros[c]
    
    print(f"A média aritimética dos números digitados é {soma/len(numeros):.2f}")


if __name__ == "__main__":
    main()