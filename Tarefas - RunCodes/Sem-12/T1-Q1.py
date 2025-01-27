# A tartaruga e a lebre vão apostar uma corrida. A lebre concede à tartaruga o direito de sair n sua frente.
# A tartaruga corre a 1 metro por minuto e a lebre corre a 10 metros por minuto. 
# Faça um programa que leia quantos metros a tartaruga sai à frente da lebre e calcule quantos 
# minutos levará até que a lebre alcance a tartaruga. 
# Por exemplo, se a tartaruga sair 
# 500 metros à frente a lebre alcança em 56 minutos.

class corrida():
    def __init__(self):
        self.user()

        
    def user(self):
        print(" CORRIDA - TARTARUGA & LEBRE ")
        print("\n*Obs: Tartaruga corre 1m por minutos\nLebre corre 10m por minuto")
        tartaruga = int(input("\nDigite quantos metros a tartaruga sai a frente\n-> "))
        print(f"\nA lebre levará {round(tartaruga/9)}min para alcançar a tartaruga.")


corrida()
