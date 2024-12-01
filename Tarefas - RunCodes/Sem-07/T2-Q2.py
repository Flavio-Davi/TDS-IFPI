# Nem sempre as transações financeiras resultam em números inteiros. 
# Vamos usar o round() para resolver isso! Peça ao usuário para inserir 
# uma quantidade de dinheiro. Em seguida, arredonde esse valor para o 
# número inteiro mais próximo e imprima o resultado.

def main():
    print(" Arredondador ".center(45, "="))
    user = float(input("\nDigite: "))
    print(f"\nO número arredondado é {round(user)}")

if __name__ == "__main__":
    main()
