# Escreva um programa que pergunte o depósito inicial e a taxa de juros ao ano de uma poupança.
# Mostre em quantos anos o valor acumulado será o dobro do valor inicial.

def calcular(valor, juros):
    anos = 0
    valor_calc = valor
    
    while valor_calc < valor*2:
        valor_calc += valor_calc * (juros/100)
        anos+=1

    return anos


def main():
    deposInic = float(input().strip())
    taxaJuro = float(input().strip())

    total = calcular(deposInic, taxaJuro)
    print(total)

if __name__ == "__main__":
    main()
