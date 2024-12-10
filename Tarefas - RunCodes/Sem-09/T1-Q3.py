# Escreva um programa que leia dois valores que correspondem à base e a altura de um retângulo. 
# O programa deve inicialmente verificar se os valores formam um retângulo ou um quadrado. 
# Caso formem um quadrado imprima a palavra QUADRADO e caso seja um retângulo, mostre o perímetro 
# (soma de todos os lados) e a área (base vezes a altura) do retângulo. Separe esses valores com um hífen.


def verificador(base, altura):
    if base == altura:
        figura = "QUADRADO"
        perimetro = base*2 + altura*2
        area = base*altura
        return figura, perimetro, area
    else:
        figura = "RETÂNGULO"
        perimetro = base*2 + altura*2
        area = base*altura
        return figura, perimetro, area

def main():
    print(" Fígura Geometrica ".center(44, "@"))
    base = int(input("Digite a base: "))
    altura = int(input("Digite a altura: "))
    
    dados = verificador(base, altura)
    descricao = ["Figura", "Perímetro", "Área"]

    print("\nDe acordo cocm os dados digitados, conclimos que:")
    for i, dado in enumerate(dados):
        print(f"{descricao[i]}: {dado}")
    

if __name__ == "__main__":
    main()
