# Escreva um programa que leia um conjunto 100 números inteiros e exiba o valor médio dos mesmos (com duas casas decimais).

def main():
    soma = 0
    all = list()

    print(" MÉDIA DE NÚMEROS ".center(30, "="))
    for c in range(1, 101):
        n = int(input(f"Escreva o {c}° número: "))
        all.append(n)
        soma+=n
        
    media = soma/len(all)
    print(f"{media:.2f}")


if __name__ == "__main__":
    main()