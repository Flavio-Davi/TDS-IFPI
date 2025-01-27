# Um número é, por definição, primo se ele não tem divisores, exceto 1 e ele próprio. 
# Escreva um programa que leia um número e determine se ele é ou não primo.

class primo():
    def __init__(self):
        self.users()


    def calculo(self, x):
        if x <= 1:
            return False
        elif x == 2:
            return True
        
        for c in range(2, round(x/2)+3):
            if x%c==0:
                return False
        return True


    def users(self):
        print(" VERIFICAÇÃO DE N° PRIMO ".center(60, "@"))
        user = int(input("\nNúmero: ").strip())
        verif = self.calculo(user)
        print(f"\nNúmero digitado: {'PRIMO' if verif == True else 'NÃO É PRIMO'}")


primo()