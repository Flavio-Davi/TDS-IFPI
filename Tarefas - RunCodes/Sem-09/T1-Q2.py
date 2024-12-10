# Escreva um programa que leia dois valores e uma das seguintes operações, codificadas dessa forma, será executada:
# 1 – Adição
# 2 – Subtração
# 3 – Multiplicação
# 4 – Divisão
# Calcule e escreva o resultado dessa operação sobre os dois valores lidos.

def operacao(valor1, valor2, operador):
    if operador == 1:
        return valor1 + valor2
    elif operador == 2:
        return valor1 - valor2
    elif operador == 3:
        return valor1 * valor2
    elif operador == 4:
        return valor1 / valor2

def main():
    print(" CALCULADORA ".center(44, "#"))
    valor1 = float(input("Digite o 1° número: "))
    valor2 = float(input("Digite o 2° número: "))
    esc = int(input("""1 – Adição
2 – Subtração
3 – Multiplicação
4 – Divisão\n>>> """))

    print(f"\nResultado: {operacao(valor1, valor2, esc):.2f}")


if __name__ == "__main__":
    main()
