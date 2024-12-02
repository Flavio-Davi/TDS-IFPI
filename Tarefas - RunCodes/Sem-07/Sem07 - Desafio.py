# Crie seu própio Quiz/Game

from random import randint

print(" GAME ".center(60, "-"))

while True:
    score = 0
    pc = randint(1, 10)
    print(f"\t\t\t\tPONTUAÇÃO [{score}/10]")
    user = int(input("Pensei em número entre 1 e 10, adivinhe qual é?\n>>> "))

    if user == pc:
        print("Você acertou!!!")
        score += 1
    else:
        print("Você errou!")
    print(pc)
    cont = input("Deseja continuar? [S / N] ").upper()
    if cont == "N":
        break