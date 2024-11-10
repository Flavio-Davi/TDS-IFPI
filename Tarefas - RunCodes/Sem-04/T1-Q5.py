# Você está fazendo uma reforma em casa e precisa calcular a quantidade de piso para 
# sua sala e a quantidade de tinta a ser usada nas paredes. Precisa também saber qual 
# o volume da sala em metros cúbicos para estimar a potência necessária para o ar condicionado. 
# Para tanto, escreva um programa que leia 3 números correspondendo ao valor da altura, comprimento e 
# largura da sala em metros e em seguida imprima:

print(" CÁLCULOS ".center(45, "="))

altura = int(input("Altura: "))
comprimento = int(input("Comprimento: "))
largura = int(input("Largura: "))

AreaPiso = largura * comprimento
VolumeSala = largura * comprimento * altura
AreaParedes = 2 * (altura * largura) + 2 * (altura * comprimento)

print(f"""\n A área do piso é: {AreaPiso}
\n O volume da sala é: {VolumeSala}
\n A area da parede é: {AreaParedes}""")
