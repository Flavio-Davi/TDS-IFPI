# Escreva um programa que leia a altura e o sexo de uma pessoa, considere 1 para 'homens' e 2 para 'mulheres'. 
# Usando duas casas decimais, calcule e mostre o peso ideal utilizando as seguintes fórmulas:

# • para homens: (72.7 * altura) – 58
# • para mulheres: (62.1 * altura) – 44.7

def Pideal(sexo, altura):
    if sexo == 1:
        return (72.7 * altura) - 58
    elif sexo == 2:
        return (62.1 * altura) - 44.7


def main():
    print(" PESO IDEAL ".center(44, "#"))
    altura = float(input("\nDigite sua altura(m): "))
    sexo = int(input("Digite o seu sexo[1-homem | 2-mulher]: "))
    print(f"\nO seu peso ideal é {Pideal(sexo, altura):.2f}")


if __name__ == "__main__":
    main()
