# Pergunte ao usuário quantos quilômetros até Marte e quantos quilômetros 
# por hora sua nave espacial pode viajar. Calcule e mostre quanto tempo levaria para chegar a Marte.
# Tempo de viagem = Distância / Velocidade média 

dist = float(input("Quantos quilômetros até Marte?\n➥ "))
velo = float(input("Lega, e quantos quilômetros por hora sua nave espacial pode viajar?\n➥ "))

Tviagem = dist/velo

print(f"\nBaseado na distância de seu ponto até marte e a velocidade máxima de sua nave é certo afirmar que o tempo que você levará para chegar em marte é de {Tviagem} horas!")