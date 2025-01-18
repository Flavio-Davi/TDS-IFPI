# Escreva um programa que leia número inteiro qualquer e mostre na forma invertida.

def main():
    user = input().strip()
    user = user[::-1]
    
    if user != "0":
        while user[0] == "0":
            user = user[1::] 
        print(user)
    else:
        print("0")


if __name__ == "__main__":
    main()
