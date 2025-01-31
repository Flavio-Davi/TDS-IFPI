# Crie um programa para criptografar e descriptografar uma cifra de Cesar.

import string 

class Cifra():
    def __init__(self):
        self.home()


    def criptografar(self, chave, msg):
        letras = string.ascii_letters
        msg_crip = ""

        for i in msg:
            for letra in range(len(letras)):
                if i == letras[letra]:
                    msg_crip += letras[letra+chave]
        
        return msg_crip


    def home(self):
        print(" CIFRA DE CÉSAR ".center(40, "#"))
        user  = input("\nDigite a mensagem que deseja criptografar: ")
        chave = int(input("\nDigite a chave de sua cifra: "))
        print(self.criptografar(chave, user))

Cifra()
