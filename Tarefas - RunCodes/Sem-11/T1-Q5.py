# Pedro recebe um salário mensal e tem aumentos salariais de 5% uma vez por ano no mês de março. Pedro também tem uma dívida no
# cartão de crédito com uma taxa de juros de 15% ao mês. Considerando que a situação se refere ao mês de outubro do ano de 2016,
# faça um programa leia o valor do salário e o valor da dívida e calcula, simulando a evolução do salário e da dívida de Pedro,
# em que mês e ano a dívida com o cartão de crédito será superior ao seu próprio salário.
# Represente os meses como inteiros de 1 a 12.
# Dica: Controle essas quatro variáveis:
# “dívida” que aumenta todo mês; “salário” que aumenta apenas se o número do mês for 3 (março); “mês” que é incrementado sempre,
# mas que retorna a 1 quando passar de 12; “ano” que só é incrementado quando o mês retornar a 1.

def calcular(vDivida, vSalario, nAno, nMes, txJuros, txSalario):
    while vDivida < vSalario:
        vDivida += vDivida*txJuros
        nMes += 1

        if nMes == 3:
            vSalario += vSalario*txSalario
        elif nMes == 12:
            nMes = 0
            nAno += 1

    return f"{nMes}/{nAno}"


def main():
    print(" CALCULADORA DE JUROS ".center(55, "#"))

    valorSalario = float(input("\nDigite o valor de seu salário: "))
    valorDivida = float(input("Digite o valor de sua dívida: "))
    mes = int(input("Digite o mês que sua dívida iniciou: "))
    ano = int(input("Digite o ano que sua dívida iniciou: "))
    juros = float(input("Digite a taxa de juros mensal de sua dívida: "))
    aumSalario = float(
        input("Digite o percentual que seu salário cresce anualmente: "))

    res = calcular(valorDivida, valorSalario, ano, mes, juros, aumSalario)

    print(f"\nSua dívida será maior que seu salário na data: {res}")


if __name__ == "__main__":
    main()
