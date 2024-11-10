# Escreva um programa que leia dois valores e mostre na tela, nessa ordem:
# a. A soma dos números;
# b. A concatenação das strings;
# c. A multiplicação dos números;
# d. A multiplicação como strings;
# e. A divisão dos números;
# f. A divisão inteira dos números;
# g. A exponenciação;
# h. O módulo (resto).

from os import system

print(" CALCULOS ".center(45, "="))
ValorA = float(input("\nValor de A: "))
ValorB = int(input("Valor de B: "))

while True:
    system("cls")
    print(" CALCULOS ".center(45, "="))
    
    menu = input("""a. A soma dos números;
b. A concatenação das strings;
c. A multiplicação dos números;
d. A multiplicação como strings;
e. A divisão dos números;
f. A divisão inteira dos números;
g. A exponenciação;
h. O módulo (resto)
i. Todas as opções a cima
j. Digitar novos valores
k. Sair
\n➥ """)

    if menu == "a":
        system("cls")
        print(f"A soma é: {ValorA+ValorB}")
        input("Digite qualquer tecla para voltar ao menu.")
        system("cls")
    elif menu == "b":
        print(f"A concatenação é: {ValorA}{ValorB}")
        input("Digite qualquer tecla para voltar ao menu.")
        system("cls")
        system("cls")
    elif menu == "c":
        system("cls")
        print(f"A multiplicação é {ValorA*ValorB}")
        input("Digite qualquer tecla para voltar ao menu.")
        system("cls")
    elif menu == "d":
        system("cls")
        print(f"A multiplicação como strings é: {str(ValorA)*ValorB}")
        input("Digite qualquer tecla para voltar ao menu.")
        system("cls")
    elif menu == "e":
        system("cls")
        print(f"A divisão é: {ValorA/ValorB:.2f}")
        input("Digite qualquer tecla para voltar ao menu.")
        system("cls")
    elif menu == "f":
        system("cls")
        print(f"A divisão inteira é: {ValorA//ValorB}")
        input("Digite qualquer tecla para voltar ao menu.")
        system("cls")
    elif menu == "g":
        system("cls")
        print(f"A exponeciação é: {ValorA**ValorB:.2f}")
        input("Digite qualquer tecla para voltar ao menu.")
        system("clear")
    elif menu == "h":
        system("cls")
        print(f"O módulo(resto da divisão) é: {ValorA%ValorB}")
        input("Digite qualquer tecla para voltar ao menu.")
        system("cls")
    elif menu == "i":
        system("cls")
        print(f"""A soma é: {ValorA+ValorB}
A concatenação é: {ValorA}{ValorB}
A multiplicação é {ValorA*ValorB}
A multiplicação como strings é: {str(ValorA)*ValorB}
A divisão é: {ValorA/ValorB:.2f}
A divisão inteira é: {ValorA//ValorB}
A exponeciação é: {ValorA**ValorB:.2f}
O módulo(resto da divisão) é: {ValorA%ValorB}""")
        input("Digite qualquer tecla para voltar ao menu.")
        system("cls")
    elif menu == "j":
        system("cls")
        ValorA = float(input("\nValor de A: "))
        ValorB = int(input("Valor de B: "))
        input("Digite qualquer tecla para voltar ao menu.")
        system("cls")
    elif menu == "k":
        system("cls")
        print("Programa finalizado, até mais!")
        break   
    else:
        continue
