# A Bate Ponto LTDA bonifica seus funcionários de acordo o tempo de 
# serviço na empresa Escreva um programa que leia o tempo de serviço 
# de um funcionário e o valor do bônus por ano trabalhado. Mostre na 
# tela quanto será a bonificação do funcionário.

Tserv = float(input("Qual o seu tempo de serviço?\n➥ "))
VbonAn = float(input("E qual o seu bônus anual?\n➥ "))

print(f"Dado o seu tempo de serviço e bbonificação anual, sua bonificação será de {Tserv*VbonAn:.2f}")
