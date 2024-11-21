# Você foi ao mercado mágico e, ao comprar 3 maçãs e 2 bananas, o caixa 
# precisa da sua ajuda para calcular o total! Leia o preço de uma maçã 
# e o preço de uma banana, calcule e imprima o total da sua compra.

def main():
    print(" Caixa ".center(45, "="))
    user = float(input("\n3 maçãs: R$"))
    user1 = float(input("2 banas: R$"))

    print(f"\nTotal............R${(user*3)+(user1*2):.2f}")

if __name__ == "__main__":
    main()
