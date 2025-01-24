# O número da sorte de uma pessoa é calculado somando os dígitos da sua data de nascimento. Escreva um
# programa que leia a data de nascimento, digitada no formado ddmmaaaa (um número inteiro com 8 dígitos), 
# e mostre o seu número da sorte. Por exemplo, quem nasceu em 29/04/1989 deve digitar 29041989 e o programa 
# vai calcular que o número da sorte é 42 (2 + 9 + 0 + 4 + 1 + 9 + 8 + 9 = 42).

class numSorte():
    def __init__(self):
        self.user()


    def calcularNum(self, data):
        num = 0
        for c in range(len(data)):
            num += int(data[c])

        return num

    def user(self):
        dataNasc = input()
        print(self.calcularNum(dataNasc))


numSorte()
