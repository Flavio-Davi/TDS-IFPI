# Dado um país A, com taxa de natalidade de 2% ao ano, e um país B com uma taxa 
# de natalidade de 3% ano. Sabe-se que, atualmente, o país A tem população maior 
# que o país B. Faça um programa que leia a população de cada país e imprima o 
# tempo necessário para que a população do país B ultrapasse a população do país A.

class crescPopul():
    def __init__(self):
        self.usuario()


    def troca(self, PaisA, PaisB):
        newPaisA = None
        newPaisB = None

        if PaisA < PaisB:
            newPaisA = PaisB
            newPaisB = PaisA
        
        return [newPaisA, newPaisB]


    def crescimento(self, paisA, paisB):
        txPaisA = 0.02
        txPaisB = 0.03
        tempo = 0
        
        if paisA < paisB: 
            newDados = self.troca(paisA, paisB)
            paisA = newDados[0]
            paisB = newDados[1]
        
        while paisA >= paisB:
            paisA += (paisA*txPaisA)
            paisB += (paisB*txPaisB)
            tempo += 1
        
        return tempo


    def usuario(self):
        B = float(input())
        A = float(input())
        print(self.crescimento(A, B))


crescPopul()
