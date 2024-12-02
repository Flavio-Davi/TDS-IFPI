# Escreva um programa que leia um número inteiro entre 10 e 99, 
# mostre uma das mensagens, a seguir, conforme o número lido.
#    Nenhum dígito é ímpar.
#    Apenas um dígito é ímpar.
#    Os dois dígitos são ímpares.

def impar(n):
    return n%2 != 0


user = input().strip()
total = 0

for num in user:
    if impar(int(num)):
        total += 1

if total == 0:
    print("Nenhum dígito é ímpar.")
else:
    print("Apenas um dígito é ímpar." if total == 1 else "Os dois dígitos são ímpares.")
