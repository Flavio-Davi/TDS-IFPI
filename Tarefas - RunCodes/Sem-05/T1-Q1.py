# Escreva um programa que ler três valores inteiros (a, b, e c). Calcule o mostre o resultado da função:
# def calcular(a, b, c):
#    return 2 * a + 5 * b - c

def calcular(a, b, c):
    return 2 * a + 5 * b - c


def main():
    ValorA = int(input("Digite o valor A: ")).strip()
    ValorB = int(input("Digite o valor B: ")).strip()
    ValorC = int(input("Digite o valor C: ")).strip()
    
    print(" Aplicando a formula ".center(45, "-"))
    print("2 x Valor A + 5 x Valor B - Valor C")
    print("-"*45)
    print(f"Resultado: {calcular(ValorA, ValorB, ValorC)}")


if __name__ == "__main__":
    main()    