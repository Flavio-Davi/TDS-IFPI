# Leia uma lista de 10 (dez) números 
# inteiros, mostre os números, sua soma e a multiplicação.

def main():
    dados = list()
    mult = 1

    print(" CÁLCULO COM LISTA DE NÚMEROS ".center(50, "#"))
    for c in range(10):
        dados.append(int(input(f"\nNúmero {c+1}: ")))
        mult *= dados[c]

    print(f"\nN° digitados: {dados}\nSoma: {sum(dados)}\nMultiplicação: {mult}")


if __name__ == "__main__":
    main()
