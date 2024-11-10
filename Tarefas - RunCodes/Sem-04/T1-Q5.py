# Você está fazendo uma reforma em casa e precisa calcular a quantidade de piso para 
# sua sala e a quantidade de tinta a ser usada nas paredes. Precisa também saber qual 
# o volume da sala em metros cúbicos para estimar a potência necessária para o ar condicionado. 
# Para tanto, escreva um programa que leia 3 números correspondendo ao valor da altura, comprimento e 
# largura da sala em metros e em seguida imprima:

altura = int(input())
comprimento = int(input())
largura = int(input())

AreaPiso = largura * comprimento
VolumeSala = largura * comprimento * altura
AreaParedes = 2 * (altura * largura) + 2 * (altura * comprimento)

print(f"""{AreaPiso}
{VolumeSala}
{AreaParedes}""")
