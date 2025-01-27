# A Sequência de Fibonacci é uma sequência de números inteiros, começando por 0 e 1, 
# na qual, cada termo subsequente corresponde à soma dos dois anteriores 
# (0, 1, 1, 2, 3, 5, 8, 13, ...). Escreva um programa que leia um número n, calcule 
# e mostre os n primeiros termos da sequência de Fibonacci. O valor lido para n sempre
# será maior ou igual a 2.
from time import sleep

class fibonacci():
    def __init__(self):
        self.user()


    def calcular(self, x):
        seq = [0, 1]

        for c in range(x-2):
            seq.append(seq[c]+seq[c+1])

        return seq
    

    def user(self):
        print(" SEQ. FIBONACCI ".center(40, "="))
        users = int(input("\nDigite o número: "))
        fib = self.calcular(users)

        print(f"\nSequência Fibonacci de {users} digitos\n")
        for c in fib:
            if c < max(fib):
                print(f"{c}", end=", ", flush=True)
                sleep(0.5)
            else:
                print(f"{c}", end=".", flush=True)
                sleep(0.5)


fibonacci()
