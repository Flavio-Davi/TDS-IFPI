# O índice de massa corporal (IMC) é uma medida internacional usada para calcular se 
# uma pessoa está no peso ideal. O IMC é determinado pela divisão da massa do indivíduo
# pelo quadrado de sua altura, em que a massa está em quilogramas e a altura em metros. 
# Escreva um programa que leia a massa (o peso) e a altura de uma pessoa e calcula o IMC
# de uma pessoa, e depois, mostra uma das seguintes mensagens:
# < 18,5 	Abaixo do peso
# < 25 	Peso normal
# < 30 	Sobrepeso
# < 35 	Obeso leve
# < 40 	Obeso moderado
# >=40 	Obeso mórbido

def imc(peso, altura):
    i = peso/altura**2

    if i < 18.5:
        return f"{i:.2f}\nAbaixo do peso"
    elif i < 25:
        return f"{i:.2f}\nPeso normal" 	
    elif i < 30:
        return f"{i:.2f}\nSobrepeso"
    elif i < 35:
        return f"{i:.2f}\nObeso leve"
    elif i < 40:
        return f"{i:.2f}\nObeso moderado"
    elif i >=40:
        return f"{i:.2f}\nObeso mórbido" 


def main():
    print(" I.M.C. ".center(30, "#"))
    pesoKg = float(input("Digite seu peso(Kg): "))
    alturaM = float(input("Digite sua altura(m): "))

    print(f"\nO resultado do calculo I.M.C foi {imc(pesoKg, alturaM)}")


if __name__ == "__main__":
    main()
