# Escreva um programa que leia um caractere e mostra uma das mensagens: 
# “vogal”, “consoante”, “número” ou “símbolo”. Observação: O cedilha “ç”, 
# caracteres acentuados, espaço em branco e outros como “símbolo”.

import string

alfabeto = string.ascii_letters
vogais = "AaEeIiOoUu"
user = input()

if user in vogais:
    print("vogal")
elif user in alfabeto and user not in vogais:
    print("consoante")
elif user.isnumeric():
    print("número")
else:
    print("símbolo")
