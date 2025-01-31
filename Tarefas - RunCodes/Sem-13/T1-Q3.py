# Escreva um programa que leia um número n. Considere uma lista com n posições, e 
# então: a) preencha com valores reais lidos pelo teclado e imprima na ordem inversa. 
# Considere até 4 (quatro) casas decimais. b) preencha com n notas lidas pelo teclado 
# e imprima as notas e a média na tela. Considere 1 (uma) casa decimal. c) preencha com 
# n letras lidas pelo teclado e imprima quantas vogais foram lidas. Imprima as consoantes.

class Analise():
    def __init__(self):
        self.home()

    
    def media(self, notas):
        return sum(notas)/len(notas) 


    def numVogais(self, letras):
        vogais = "aeiou"
        total = 0

        for letra in letras:
            for vogal in vogais:
                if letra.lower() == vogal:
                    total += 1
        return total


    def home(self):
        print(" ANÁLISE DE LISTAS ".center(50, "#"))
        print("""\nLista A: Apresentará a ordem inversa, apenas números
Lista B: Digite as notas, apresentaremos a média.
Lista C: Apresentará o número de vogais e uma lista com as consoantes.""")
        n = int(input("\nDigite o n° de itens que será nas suas 3 listas: "))
        lista_A = list() # ordem inversa
        lista_B = list() # notas e a média na tela
        lista_C = list() # quantas vogais foram lidas
        vogais = "aeiou"

        for _ in range(n):
            lista_A.insert(0, float(input("Lista A: ")))
        for _ in range(n):
            lista_B.append(float(input("Lista B: ")))
        for _ in range(n):
            lista_C.append(input("Lista C: ").strip())

        if n != 0:
            print(f"\nLista A, ordem inversa: {lista_A}")
            print(f"Lista B: {lista_B}")
            print(f"Média de notas: {self.media(lista_B):.1f}")
            print(f"N° de vogais: {self.numVogais(lista_C)}")
            print(f"Consoantes: {[consoante for consoante in lista_C if consoante.lower() not in vogais]}")
        else:
            print("""[]
[]
SEM NOTAS
0
[]""")


if __name__ == "__main__":
    Analise()
