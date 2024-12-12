# Escreva um programa que leia 3 valores inteiros. Determine se é o segundo ou o terceiro 
# valor lido que possui menor diferença com relação ao primeiro, imprimindo o valor da diferença.

def diferenca(numeros):
    primeiro = numeros.copy()[0]

    if primeiro > numeros[1]:
        dif1 = primeiro - numeros[1]
    elif primeiro < numeros[1]:
        dif1 = numeros[1] - primeiro
    if primeiro > numeros[2]:
        dif2 = primeiro - numeros[2]
    elif primeiro < numeros[2]:
        dif2 = numeros[2] - primeiro

    return dif1 if dif1 < dif2 else dif2 


def main():
    valores = list()
    print(" COMPARATIVO ".center(44, "#"))
    print("\nDigite a baixo 3 números para descobrir a menor diferença dos dois ultimos em comparação ao terceiro.\n")
    for c in range(1, 4):
        valores.append(int(input(f"N° {c}: ").strip()))

    print(f"\nA menor diferrença existente é {diferenca(valores)}!")


if __name__ == "__main__":
    main()
