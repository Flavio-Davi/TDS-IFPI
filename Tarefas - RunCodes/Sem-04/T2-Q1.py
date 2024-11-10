# Escreva um programa que leia dois valores e mostre na tela, nessa ordem:
# a. A soma dos números;
# b. A concatenação das strings;
# c. A multiplicação dos números;
# d. A multiplicação como strings;
# e. A divisão dos números;
# f. A divisão inteira dos números;
# g. A exponenciação;
# h. O módulo (resto).

ValorA = float(input())
ValorB = int(input())

print(f"""{ValorA+ValorB}
{ValorA}{ValorB}
{ValorA*ValorB}
{str(ValorA)*ValorB}
{ValorA/ValorB}
{ValorA//ValorB}
{ValorA**ValorB}
{ValorA%ValorB}""")
