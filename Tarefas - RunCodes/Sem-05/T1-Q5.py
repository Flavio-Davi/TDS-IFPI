# Leia um número inteiro entre 1000 e 9999 e mostre o número na ordem inversa. 
# Por exemplo, se o número lido for 5678 deverá ser mostrado 8765.
from os import system
from time import sleep

def inverter(number):
    return f"{number}"[::-1]


def main():
    print("\033[1;32m"+"-"*38)
    print("\tINVERSÃO DE NUMERAL")
    print("-"*38)
    
    while True: 
     
        user = int(input("\033[1;32m"+"\nDigite um número entre (1000 - 9999): ")).strip()
        
        if user<1000 or user>9999:
            print("\033[1;31m"+"ERROR: Número inválido, digite um número válido.")
            sleep(0.5)
            system("clear")
            continue
        else:
            print(f"O número invertido é {inverter(user)}")
            break


if __name__ == "__main__":
    main()
