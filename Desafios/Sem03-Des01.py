# Seu programa até agora só diz às pessoas quantos anos elas terão no ano 2025. 
# E se alguém quiser saber quantos anos terá no ano 2050? Ou no ano 3000? Adicione 
# outra variável no seu programa, de modo que o usuário consiga saber quantos anos 
# ele terá em qualquer ano que ele escolher.

AnoNasc = int(input("Em que ano você nasceu?\n➥ "))
AnoIda = int(input("Para qual ano você quer saber sua idade?\n➥ "))

print(f"No ano {AnoIda} você terá {AnoIda-AnoNasc} anos!")
