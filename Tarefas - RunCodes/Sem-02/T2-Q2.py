# Escreva um programa de leia o preço de um produto e mostre na tela 
# o valor com 10% de desconto arredondado para duas casas decimais.

try:
    preco = float(input("Qual o preço do produto que deseja comprar?\n➥ "))
    desconto = preco - (preco*0.10)
    print(f"Parabéns, vocÊ ganhou 10% de desconto, o valor á ser pago é de R${desconto:.2f}")
except:
    print("Programa encerrado!")
