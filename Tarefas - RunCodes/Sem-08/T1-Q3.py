# Escreva um programa que leia 5 números inteiros e escreva o maior e o menor deles. 
# Considere que todos os valores são diferentes. NÃO use as funções min() e max().

def maior_menor(numeros):
    maior = 0
    menor = numeros[0]
    list_rev = numeros[::-1]

    for c in range(len(numeros)):
        if numeros[c] > maior:
            maior = numeros[c]
    
    for i in range(len(numeros)):
        for b in range(len(list_rev)):
            if numeros[i] < list_rev[b] and numeros[i] < menor:
                menor = numeros[i]

    return maior, menor 


def main():
    num = list()

    print(" Maior & Menor ".center(44, "#"))
    for c in range(1, 6):
        num.append(int(input(f"Digite o {c}° número: ")))

    max_min = maior_menor(num)
    print(f"O maior número digitado é {max_min[0]}\nE o menor é {max_min[1]}")


if __name__ == "__main__":
    main()