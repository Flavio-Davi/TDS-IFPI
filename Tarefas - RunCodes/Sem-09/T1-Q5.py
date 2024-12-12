# Escreva um programa que leia um número inteiro e calcule o resto da divisão inteira do número 
# lido por 5 (cinco). A seguir, de acordo com o resultado da divisão, faça o que é solicitado abaixo:
#    Se 0 (zero), escreva a o resultado da equação 9n + 7, onde n é o valor lido;
#    Se 1 (um), escreva se o valor lido é par ou ímpar;
#    Se 2 (dois), escreva a o resultado da equação 5n2 – 3n + 42, onde n é o valor lido;
#    Se 3 (três), escreva a divisão inteira do valor lido por 10;
#    Se 4 (quatro), escreva o quadrado do valor lido;

def se(x):
    ValorOriginal = x
    x = x%5
    if x == 0:
        return (9*ValorOriginal) + 7
    elif x == 1:
        return "par" if ValorOriginal%2 == 0 else "ímpar"
    elif x == 2:
        return 5*(ValorOriginal**2) - (3*ValorOriginal) + 42
    elif x == 3:
        return ValorOriginal // 10
    elif x == 4:
        return ValorOriginal**2


def main():
    print("""De a cordo com o resto da divisão do número digitado ocorrerá:\n 
Se 0 (zero), apresentará o resultado da equação 9n + 7, onde n é o valor lido;
Se 1 (um), apresentará se valor lido é par ou ímpar;
Se 2 (dois), apresentará o resultado da equação 5n2 – 3n + 42, onde n é o valor lido;
Se 3 (três), apresentará a divisão inteira do valor lido por 10;
Se 4 (quatro), apresentará o quadrado do valor lido;\n\n""")
    
    num = int(input("Digite o número: ").strip())
    print(f"Resultado: {se(num)}")


if __name__ == "__main__":
    main()
