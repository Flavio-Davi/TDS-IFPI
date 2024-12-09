# Escreva um programa que leia 5 números inteiros, calcule e mostre a média 
# e escreva os que são maiores que a média. Considere duas casas decimais.

def maior_med(nums):
    maiores = list()
    media = 0
    for i in nums:
        media += i
    media /= 5

    for b in nums:
        if b > media:
            maiores.append(b)
    return maiores


def main():
    nums = list()

    print(" Maior que a média ".center(50, "@"))
    for c in range(1, 6):
        nums.append(int(input(f"Digite o {c}° número: ")))   

    print(f"O(s) número(s) digitados que são a cima da média é {", ".join(map(str, maior_med(nums)))}")


if __name__ == "__main__":
    main()
