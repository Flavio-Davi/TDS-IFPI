# Adicione mais cumprimento

from random import choice

print("Gerador de cumprimento")
print("-"*40)

adjetivos = ["MARAVILHOSO", "A CIMA DA MÉDIA", "EXCELENTE", "SENCAIONAL", "EXPERT"]
hobbies = ["ANDAR DE BICICLETE", "PROGRAMAR", "FAZER CHÁ"]

nome = input("Qual o seu nome?\n>>>")
print(f"Aqui está seu cumprimento {nome}")

print(f"{nome} você é {choice(adjetivos)} em {choice(hobbies)}")
print("De nada!")
