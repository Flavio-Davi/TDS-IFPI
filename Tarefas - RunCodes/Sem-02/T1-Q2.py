# Desenvolva um programa que pergunte a distância até um planeta em 
# quilômetros e a velocidade da nave em km/h. Informe quantos dias e 
# quantas horas a viagem levará, considerando 24 horas por dia.

distKm = float(input("Qual a distância até Saturno e Km?\n➥ "))
VnavKm = float(input("E qual a velocidade da em Km/h que usará?\n➥ "))
# Horas de viagem: dividir a distância pelo número de quilômetros por hora.
Thoras = distKm/VnavKm
Dviagem = Thoras//24

Hviagem = Thoras % 24
print(f"\nA previsão de chega é de {Dviagem:.0f} dias e {Hviagem:.0f} horas. Faça uma boa viagem!")
