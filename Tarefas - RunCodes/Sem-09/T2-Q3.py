# Escreva um programa que leia uma data no formado DDMMAAA e informe se é uma data válida.
# OBS: Use apenas condicionais e os tipos básicos do Python; Não utilize bibliotecas do Python 
# que tratam datas; Considere que em anos bissextos o mês de fevereiro tem 29 dias.

def bissexto(ano):
    return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

def validar_data(data):
    if len(data) != 8:
        return False
    
    dia = int(data[:2])
    mes = int(data[2:4])
    ano = int(data[4:])

    if mes < 1 or mes > 12 or dia < 1:
        return False

    if mes in {4, 6, 9, 11}:
        return dia <= 30
    elif mes == 2:
        if bissexto(ano):
            return dia <= 29
        else:
            return dia <= 28
    else:
        return dia <= 31


def main():
    print(" VALIDADOR DE DATAS ".center(60, "^"))
    data = input("Digite a data [DDMMAAA]: ")
    
    if validar_data(data):
        print(f"A data é válida!")
    else:
        print(f"A data é inválida!")


if __name__ == "__main__":
    main()
