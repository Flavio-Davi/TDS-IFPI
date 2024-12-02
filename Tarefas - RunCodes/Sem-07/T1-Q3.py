# Escreva um programa que leia a cor de um sinal de trânsito 
# (“V” é verde; “A” é amarelo; “E” é vermelho) e retorne a respectiva mensagem 
# “Siga”, “Atenção”, ou “Pare”. Assuma entradas válidas.

user = input().upper()[0]

op = {"V": "Siga", "A": "Atenção", "E": "Pare"}

print(op.get(user))
