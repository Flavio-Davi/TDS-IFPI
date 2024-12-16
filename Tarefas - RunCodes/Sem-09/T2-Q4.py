# Um sacolão está vendendo frutas com a seguinte tabela de preços:
# Item 	    Até 5Kg 	 Acima de 5Kg
# Morango 	R$ 2,50 	  R$ 2,20
# Maça 	    R$ 1,80 	  R$ 1,50
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar 
# R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um programa que
# leia a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva
#  o valor a ser pago pelo cliente.

def mercado(morango, maca):
    preco_morango = 2.5 if morango <= 5 else 2.2
    preco_maca = 1.8 if maca <= 5 else 1.5
    
    total = (morango * preco_morango) + (maca * preco_maca)
    
    if (morango + maca) > 8 or total > 25:
        total *= 0.90
    
    return total


def main():
    print("  SUPERMERCADO DO SEU ZÉ ".center(50, "#"))
    morango = float(input("Quantidade de morangos (Kg): ").strip())
    maca = float(input("Quantidade de maçãs (Kg): ").strip())
    total = f"{mercado(morango, maca):.2f}".replace(".", ",")
    print(f"Valor total R${total}")


if __name__ == "__main__":
    main()
