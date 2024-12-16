# Escreva um programa que leia um número inteiro menor que 1000 e mostre por extenso a 
# quantidade de centenas, dezenas e unidades do número lido, observando os termos no plural, 
# a colocação do "e" ou da vírgula entre valores e o ponto “.” no final da frase. Exemplos:
#    521 = cinco centenas, duas dezenas e uma unidade.
#    107 = uma centena e sete unidades.
#    80 = oito dezenas.

def extenso(numero):
    numeros = ["uma", "duas", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez"]
    NumAlgarismo = ["centena", "dezena", "unidade"]
    frase = ""

    if 0 < numero < 10:
        if numero > 1:    
            frase += f"{numeros[numero-1]} {NumAlgarismo[2]}s."
        else:
            frase += f"{numeros[numero-1]} {NumAlgarismo[2]}."

    elif 10 <= numero < 100:
        dezena = int(str(numero)[0])
        unidades = int(str(numero)[1])
        if dezena == 1 and unidades > 1:
            frase += f"{numeros[dezena-1]} {NumAlgarismo[1]} e {numeros[unidades-1]} {NumAlgarismo[2]}s."
        elif dezena == 1 and unidades == 0:
            frase += f"{numeros[dezena-1]} {NumAlgarismo[1]}"
        elif unidades > 1:    
            frase += f"{numeros[dezena-1]} {NumAlgarismo[1]}s e {numeros[unidades-1]} {NumAlgarismo[2]}s."
        elif unidades == 1:
            if dezena == 1:
                frase += f"{numeros[dezena-1]} {NumAlgarismo[1]} e {numeros[unidades-1]} {NumAlgarismo[2]}"
            else:    
                frase += f"{numeros[dezena-1]} {NumAlgarismo[1]}s e {numeros[unidades-1]} {NumAlgarismo[2]}"
        else:
            frase += f"{numeros[dezena-1]} {NumAlgarismo[1]}s."
        
    elif 100 <= numero < 1000:
        centena = int(str(numero)[0]) 
        dezena = int(str(numero)[1])
        unidades = int(str(numero)[2])
        
        if centena >= 1 and dezena >= 1 and unidades >= 1:
            if dezena > 1 and centena > 1:
                if unidades > 1:
                    frase += f"{numeros[centena-1]} {NumAlgarismo[0]}s, {numeros[dezena-1]} {NumAlgarismo[1]}s e {numeros[unidades-1]} {NumAlgarismo[2]}s."
                else:
                    frase += f"{numeros[centena-1]} {NumAlgarismo[0]}s, {numeros[dezena-1]} {NumAlgarismo[1]}s e {numeros[unidades-1]} {NumAlgarismo[2]}."
            elif dezena == 1 and unidades == 1 and centena == 1:
                frase += f"{numeros[centena-1]} {NumAlgarismo[0]}, {numeros[dezena-1]} {NumAlgarismo[1]} e {numeros[unidades-1]} {NumAlgarismo[2]}."
            elif unidades > 1:
                    if dezena > 1:
                        frase += f"{numeros[centena-1]} {NumAlgarismo[0]}, {numeros[dezena-1]} {NumAlgarismo[1]}s e {numeros[unidades-1]} {NumAlgarismo[2]}s."
                    else:
                        frase += f"{numeros[centena-1]} {NumAlgarismo[0]}, {numeros[dezena-1]} {NumAlgarismo[1]} e {numeros[unidades-1]} {NumAlgarismo[2]}s."              
            elif dezena > 1:
                frase += f"{numeros[centena-1]} {NumAlgarismo[0]}, {numeros[dezena-1]} {NumAlgarismo[1]}s e {numeros[unidades-1]} {NumAlgarismo[2]}."
            elif centena > 1:
                frase += f"{numeros[centena-1]} {NumAlgarismo[0]}s, {numeros[dezena-1]} {NumAlgarismo[1]} e {numeros[unidades-1]} {NumAlgarismo[2]}."          
            elif centena == 1:
                frase += f"{numeros[centena-1]} {NumAlgarismo[0]}, {numeros[dezena-1]} {NumAlgarismo[1]}s e {numeros[unidades-1]} {NumAlgarismo[2]}s."
            else:
                frase += f"{numeros[centena-1]} {NumAlgarismo[0]}s, {numeros[dezena-1]} {NumAlgarismo[1]}s e {numeros[unidades-1]} {NumAlgarismo[2]}s."
        elif dezena == 0 or unidades == 0:
            if dezena == 0 and unidades > 1 and centena > 1:
                frase += f"{numeros[centena-1]} {NumAlgarismo[0]}s e {numeros[unidades-1]} {NumAlgarismo[2]}s."
            elif dezena == 0 and unidades > 1 and centena == 1:
                frase += f"{numeros[centena-1]} {NumAlgarismo[0]} e {numeros[unidades-1]} {NumAlgarismo[2]}s."
            elif dezena == 0 and unidades == 1 and centena > 1:
                frase += f"{numeros[centena-1]} {NumAlgarismo[0]}s e {numeros[unidades-1]} {NumAlgarismo[2]}."
            elif dezena == 0 and unidades == 1 and centena >= 1:
                frase += f"{numeros[centena-1]} {NumAlgarismo[0]} e {numeros[unidades-1]} {NumAlgarismo[2]}."
            elif dezena > 0 and unidades == 0:
                if centena == 1 and dezena == 1 and unidades == 1:
                    frase += f"{numeros[centena-1]} {NumAlgarismo[0]}, {numeros[dezena-1]} {NumAlgarismo[1]} e {numeros[unidades-1]} {NumAlgarismo[2]}."
                elif centena == 1 and dezena > 1 and unidades == 1:
                    frase += f"{numeros[centena-1]} {NumAlgarismo[0]}, {numeros[dezena-1]} {NumAlgarismo[1]}s e {numeros[unidades-1]} {NumAlgarismo[2]}."
                elif centena == 1 and dezena == 1 and unidades > 1:
                    frase += f"{numeros[centena-1]} {NumAlgarismo[0]}, {numeros[dezena-1]} {NumAlgarismo[1]} e {numeros[unidades-1]} {NumAlgarismo[2]}s."
                elif centena == 1 and dezena == 1 and unidades == 0:
                    frase += f"{numeros[centena-1]} {NumAlgarismo[0]} e {numeros[dezena-1]} {NumAlgarismo[1]}"
                elif centena > 1 and dezena == 1 and unidades == 1:
                    frase += f"{numeros[centena-1]} {NumAlgarismo[0]}s, {numeros[dezena-1]} {NumAlgarismo[1]} e {numeros[unidades-1]} {NumAlgarismo[2]}."
                elif centena > 1 and dezena == 1 and unidades == 0:
                    frase += f"{numeros[centena-1]} {NumAlgarismo[0]}s e {numeros[dezena-1]} {NumAlgarismo[1]}."
                elif centena > 1 and dezena > 1 and unidades > 1:
                    frase += f"{numeros[centena-1]} {NumAlgarismo[0]}s, {numeros[dezena-1]} {NumAlgarismo[1]}s e {numeros[unidades-1]} {NumAlgarismo[2]}s."
                elif centena >= 1 and dezena >= 1 and unidades == 0:
                    if dezena == 1:
                        frase += f"{numeros[centena-1]} {NumAlgarismo[0]}s e {numeros[dezena-1]} {NumAlgarismo[1]}."
                    elif centena == 1:
                        frase += f"{numeros[centena-1]} {NumAlgarismo[0]}, {numeros[dezena-1]} {NumAlgarismo[1]}s"
                    else:
                        frase += f"{numeros[centena-1]} {NumAlgarismo[0]}s e {numeros[dezena-1]} {NumAlgarismo[1]}s."
            else:
                frase += f"{numeros[centena-1]} {NumAlgarismo[0]}."

    return frase


def main():
    print(" ALGARISMOS POR EXTENSO (VERSÃO BETA) ".center(70, "@"))
    user = int(input("\nDigite o número para visualizar os algarismos em extenso(De 0 à 1000): ").strip())
    print(f"\n{extenso(user)}")


if __name__ == '__main__':
    main()
