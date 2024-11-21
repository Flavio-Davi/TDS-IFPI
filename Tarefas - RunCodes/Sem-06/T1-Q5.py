# Você é dono de uma loja que vende roupas. Sua política é de dar desconto para quem compra à vista, 
# vender pelo preço de etiqueta para quem paga em 5 vezes e cobrar jutos de quem comprar em 10 vezes. 
# Escreva um programa que leia o valor de uma compra e imprima três valores, todos com até duas casas decimais:
#    Valor para pagamento à vista, com desconto de 9%.
#    Valor da prestação para pagamento em 5 vezes, sem desconto nem juros.
#    Valor da prestação para pagamento em 10 vezes, com 17% de juros.

def loja(preco):
    PgAvista = preco - (preco*0.09)
    PgPrazo5 = preco/5
    PgPrazo10 = (preco*1.17)/10

    return round(PgAvista, 2), round(PgPrazo5, 2), round(PgPrazo10, 2)


def main():
    print(" Loja do Zé ".center(45, "="))

    user = float(input("\nPreço: R$"))
    inf = ["Pagamento a vista(9% de desconto)", "Divido em 5x(Sem juros)", "Divido em 10x(17% de juros)"]
    for c in range(3):
        print(f"\n{inf[c]}: R${loja(user)[c]}".replace(".", ","))


if __name__ == "__main__":
    main()
