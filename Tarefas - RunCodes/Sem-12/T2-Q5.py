# Escreva um programa que leia dois valores inteiros (x e y) e mostre todos os números primos entre x e y.

def calculo(x):
        if x <= 1:
            return False
        elif x == 2:
            return True
        
        for c in range(2, round(x/2)+3):
            if x%c==0:
                return False
        return True


def main():
    dados = list()
    dados.append(int(input().strip()))
    dados.append(int(input().strip()))

    cont = [primo for primo in range(min(dados), max(dados)+1) if calculo(primo)]
        
    print("\n".join(map(str, cont)))


if __name__ == "__main__":
     main()