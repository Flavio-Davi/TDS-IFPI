# Você é um aprendiz de feiticeiro encarregado de preparar uma poção mágica especial. 
# Para isso, você precisa de porções dos ingredientes mágicos Pó de Lua Estelar, Essência de Dragão 
# e Lágrimas de Fênix. No entanto, cada ingrediente tem um preço diferente no mercado mágico. 
# O ingrediente Pó de Lua Estelar custa 5 moedas de ouro por porção, Essência de Dragão custa 3 moedas 
# de ouro por porção, e o Lágrimas de Fênix custa 8 moedas de ouro por porção. O programa deve começar 
# perguntando quantas porções de cada ingrediente são necessárias para a poção que você está preparando. 
# Depois, o programa deve calcular o custo total baseado na quantidade de cada ingrediente e seus respectivos 
# preços. Finalmente, o programa deve mostrar o custo total para preparar a poção. Por exemplo, 
# se a porção tem 2 Pó de Lua Estelar, 3 Essência de Dragão e 1 Lágrima de Fênix o custo total será: 
# (2 * 5) + (3 * 3) + (1 * 8) = 27 (o custo total será de 27 moedas de ouro)

print(" MERCADO MÁGICO ".center(45, "#"))

PorcEst = int(input(f"Quantas porções de Pó de Lua Estelar você precisa?\n➥ "))
PorcDra = int(input(f"Quantas porções de Essência de Dragão você precisa?\n➥ "))
PorcFen = int(input(f"Quantas porções de Lágrima de Fênix você precisa?\n➥ "))

print(f"O custo total será de {(PorcEst*5)+(PorcDra*3)+(PorcFen*8)} moedas de ouro! Bom preparo :)!")
