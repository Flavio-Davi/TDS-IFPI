# Escreva um programa que leia um preço e um valor percentual. Informe o preço 
# com o aumento percentual e o preço com o desconto percentual. Por exemplo, 
# se for lido um preço de 100.00 e o valor percentual de 5 o programa deve mostrar 
# que o preço com aumento é 105.00 e o preço com desconto é 95.00.

def  calculo(valor, percentual):
    return valor + (percentual/100*valor)


def main():
    print("-="*22)
    print("\tCALCULO PERCENTUAL, P/ MAIS")
    print("-="*22)

    userPreco = float(input("\nDigite o preço: R$")).strip()
    userPorcent = float(input("Digite um percentual (%): ")).strip()
    
    print(f"O valor do produto acrecido de {userPorcent}% é R${calculo(userPreco, userPorcent):.2f}")


if __name__ == "__main__":
    main()
