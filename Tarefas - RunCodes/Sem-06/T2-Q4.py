# Um alienígena chamado Zob precisa de ajuda para converter anos terrestres 
# em anos espaciais! Sabendo que 1 ano terrestre equivale a meio ano espacial, 
# calcule e imprima uma idade inserida pelo usuário em anos espaciais.

def main():
    print(" Anos tererestres p/ espaciais ".center(60, "="))
    user = int(input("\nDigite quantos anos deseja converter: "))
    print(f"\n{user} anos terrestres equivale à {user//2} anos espaciais")

if __name__ == "__main__":
    main()
