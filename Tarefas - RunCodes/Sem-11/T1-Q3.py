# Escreva um programa que leia uma quantidade indefinida de números inteiros positivos terminada pelo
# número 0 (zero). Ao final, o programa deve mostrar o maior e o menor de todos os números lidos
# (excluindo o zero).


def main():
    print(" MAIOR & MENOR ".center(50, "#"))
    all = list()
    user = int(input("Digite: "))
    all.append(user)

    while user != 0:
        user = int(input("Digite: "))
        all.append(user)
    all.remove(0)
    
    print(f"Números digitados: {", ".join(map(str, all))}")
    print(f"\nMaior n° digitado: {max(all)}\nMenor n° digitado: {min(all)}")

if __name__ == "__main__":
    main()
