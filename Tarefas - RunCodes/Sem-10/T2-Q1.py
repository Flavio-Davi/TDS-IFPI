# Escreva um programa que gera a letra da canção muito popular entre os programadores: 
# 99 bugs no software, pegue um deles e conserte... 100 bugs no software, pegue um deles e conserte... 
# 101 bugs no software, pegue um deles e conserte... ... Faça o programa de forma a gerar a letra da 
# música com o número de bugs no software variando de 99 a 250.

def main():
    musica = "bugs no software, pegue um deles e conserte..."
    for c in range(99, 251):
        print(f"{c} {musica}")


if __name__ == "__main__":
    main()