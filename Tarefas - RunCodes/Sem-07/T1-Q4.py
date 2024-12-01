# Escreva um programa/algoritmo que leia 5 (cinco) números inteiros e escreva na tela:
#    o maior número lido;
#    o menor número lido;
#    a média aritmética dos números lidos.

def varios(numbers):
    maior = max(numbers)
    menor = min(numbers)
    media = sum(numbers)/len(numbers)

    return maior, menor, media


def main():
    print(" Maior/Menor/Media ".center(50, "="))

    all = list()

    for c in range(1, 6):
        user = all.append(int(input(f"\nDigite o {c}° número: ")))

    mmm = ["Maior", "Menor", "Média"]
    for c in range(3):
        print(f"{mmm[c]}: {varios(all)[c]}")


if __name__ == "__main__":
    main()
