from os import name

class revisao_funcoes:
    def __init__(self):
        valido = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']


    def home(self):
        while True:
            menu = input("""
#######################
        M E N U
#######################
                 
[ 1 ] - Questão 1
[ 2 ] - Questão 2
[ 3 ] - Questão 3
[ 4 ] - Questão 4
[ 5 ] - Questão 5
[ 6 ] - Questão 6
[ 7 ] - Questão 7
[ 8 ] - Questão 8
[ 9 ] - Questão 9
[ 10 ] - Questão 10
[ 11 ] - Questão 11
[ 12 ] - Questão 12
[ 13 ] - Questão 13
[ 14 ] - Questão 14
[ 15 ] - Questão 15
[ 16 ] - Encerrar
                         
→ """)
            if menu in self.valido:
                break
        return menu


    def atv1(x):
        return False if x%2 else True



def main():
    i = revisao_funcoes()
    while True:
        user = i.home()
        if user == "16":
            print()
    if menu in valido:
        if menu == '1':
            n = int(input("Digite um número inteiro: "))
            print(f"\nO número digitado é {'par' if atv1(n) else 'impar'}")


if __name__ == '__main__':
    main()
