# Escreva um programa que leia uma quantidade de minutos e mostre 
# a quantidade de horas e minutos equivalente.
# Formato:10h0min

print(" CONVERSOR DE MINUTOS EM HORAS ".center(50, "#"))
min = float(input("Quantidade de minustos: "))

horas = min//60
minut = min%60

print(f"{min} minutos convertido para horas é {horas:.0f}h{minut:.0f}min")
