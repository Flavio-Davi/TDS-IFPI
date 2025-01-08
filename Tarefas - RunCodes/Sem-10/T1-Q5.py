# Escreva um programa que leia um conjunto de 100 números inteiros positivos e determine o maior deles.

def maior(x):
    mais = 0
    for c in range(len(x)):
        if x[c] > mais:
            mais = x[c]
    return mais
    
def main():
    print(" MAIOR N° DIGITADO ".center(55, "="))
    user = int(input("Quantos n° vocÊ deseja digitar? "))    
    
    all = list()

    for c in range(user):
        n = int(input(f"Digite o {c+1}° número: "))
        all.append(n)
        
    print(f"O maior n° digitado é {maior(all)}.")

if __name__ == "__main__":
    main()
    