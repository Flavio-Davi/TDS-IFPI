# Escreva um programa que leia o valor de um raio, calcule e mostre na
# tela o comprimento da circunferência, a área do círculo, a área da esfera e o 
# volume da esfera para o valor do raio lido. Mostre os valores com 6 casas decimais.

pi = 3.141592
try:
    raio = float(input("Digite o valor do raio\n➥ "))
    # Comprimento da circunferência, C = 2πr
    CompCirc = 2*pi*raio
    # Área de um círculo, A = π r²
    AreaCirc = pi*(raio**2)
    #  Área da esfera, A=4*πr²
    AreaEsfe = (4*pi)*(raio**2) 
    # Volume de uma esfera, V = 4/3 π r³
    VoluEsfe = 4/3 * pi * raio**3

    print(f"\nDado o valor do raio de {raio}:")
    print(f"\nO coprimento da circunferência é {CompCirc:.6f}")
    print(f"\nA área do circulo é {AreaCirc:.6f}")
    print(f"\nA área da esfera é {AreaEsfe:.6f}")
    print(f"\nO volume da esfera é {VoluEsfe:.6f}")
except:
    print("0.000000")
    print("0.000000")
    print("0.000000")
    print("0.000000")
