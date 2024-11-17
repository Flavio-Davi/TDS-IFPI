# Escreva um programa que ler o valor para um lado de um quadrado. 
# Calcule o mostre a área e o perímetro desse quadrado.

def AreaPerimetro(lado):
    area = lado ** 2
    perimetro = lado * 4

    return area, perimetro


def main():
    print("-"*65)
    print("\tCALCULADORA DE AREA & PERÍMETRO DE UM QUADRADO")
    print("-"*65)

    user = float(input("\nDigite o lado do quadradro: ")).strip()
    
    print(f"A área e perímetro respectivamente é {AreaPerimetro(user)}")


if __name__ == "__main__":
    main()