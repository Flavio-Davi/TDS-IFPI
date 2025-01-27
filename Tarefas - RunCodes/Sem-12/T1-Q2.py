# Você tem uma poupança de 10 mil reais, que rende 0,7% ao mês. Você deseja 
# comprar um carro, mas o preço do carro sobe a taxa de 0,4% ao mês. 
# Escreva um programa que leia o preço de um carro hoje e calcule em quantos
# meses, com o dinheiro dessa aplicação, você terá dinheiro suficiente para comprar o carro à vista.

class comprarCarro():
    def __init__(self):
        self.usuario()


    def calcular(self, vCarro): 
        poupanca = 10000
        rendimento = 0.007
        txCarro = 0.004
        meses = 0

        while poupanca < vCarro:
            poupanca += (poupanca*rendimento)
            vCarro += (vCarro*txCarro)
            meses += 1
    
        return meses
    

    def usuario(self):
        print(" CALCULADORA DE SONHO ".center(50, "@"))
        user = float(input("Digite o preço do carro: R$"))
        print(f"\nVocê levará {self.calcular(user)} meses para comprar o carro.")


comprarCarro()
