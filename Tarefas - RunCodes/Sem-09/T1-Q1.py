# Escreva um programa que leia 3 (três) números inteiros e escreva
# uma das mensagens abaixo, de acordo com os valores a lidos:
# • Todos os valores são diferentes;
# • Existem dois valores iguais e um diferente;
# • Todos os valores são iguais;

def definir(numeros):
    diferente = 0
    iguais = 0
    for numero in numeros:
        for numeru in numeros:
            if numero == numeru:
                iguais += 1
            elif numero != numeru:
                diferente += 1     
                
    if diferente == 4:
        return "Existem dois valores iguais e um diferente"
    elif diferente >= 3:
        return "Todos os valores são diferentes"
    elif iguais >= 3:
        return "Todos os valores são iguais"


def main():
    nums = list()
    print(" DIFERENCIAÇÃO DE NÚMEROS ".center(50, "#"))
    for c in range(1, 4):
        nums.append(input(f"Digite o {c}° número: ").strip())
    print(f"\n>>> {definir(nums)}")

if __name__ == "__main__":
    main()
