from os import name, system

def limpar():
    if name == 'nt':
        return system("cls")
    else:
        return system("clear")


class revisao_funcoes:
    def __init__(self):
        self.valido = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']


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
            limpar()
            if menu in self.valido:
                limpar()
                break
        return menu


    def atv1(self, x):
        return False if x%2 else True


    def atv2(self, raio: str, opc=1):
        if opc == 1:
            return 3.14 * raio
        elif opc == 2:
            return 3.14 * 2 ** raio
        else:
            raise("ERROR: 1 para ÁREA e 2 para PERÍMETRO.")


    def atv3(self, f: float):
        c = ((f-32)/9)*5
        return c


    def atv4(self, n1: float, n2: float):
        m = (n1+n2)/2
        if m >= 6:
            return "PARABÉNS! Você foi aprovado!"
        else:
            return "Você está de recuperação, pois não atingiu a média mínima de 6.0"


    def atv5(self, altura: float, sexo: int):
        if sexo not in [1, 2]:
            raise "ERROR: Sexo inserido inválido, digite 1 para feminino e 2 para masculino."
        elif sexo == 1:
            return (62.1 * altura)-44.7
        else:
            return (72.7 * altura)-58


    def atv6(self, l: int, m: float):
        p = l*m
        if l not in [3,4,5]:
            raise "ERRO: Apenas os valores 3, 4 ou 5 são aceitos para número de lados."
        elif l == 3:
            return f"TRIÂNGULO\nPerímetro: {p}"
        else:
            return f"QUADRADO\nPerímetro: {p}"if l == 4 else f"PENTÁGONO\nPerímetro: {p}"


    def atv7(self, n: int):
        fat = n
        if n == 1:
            return n
        else:
            for c in range(n-1, 1, -1):
                fat *= c
            return fat


    def atv8(self, caracter: str):
        if caracter in ['S', 'N']:
            return caracter
        else:
            return "Caractere inválido. Digite novamente"


    def atv9(self, n1: int, n2: int):
        tot = list(range(n1, n2+1, 1))
        return sum(tot)


    def atv10(self, a: list, b: list):
        max_a = 0
        max_b = 0
        for c in a:
            if c>max_a:
                max_a = c
        for c in b:
            if c>max_b:
                max_b = c
        return max_a, max_b


    def atv11(self, n: int):
        divisiveis = []
        for c in range(1, n+1):
            if n%c==0:
                divisiveis.append(c)
        return divisiveis


    def atv12(self, n: int):
        s = 0
        for c in range(1, n+1):
            s += c
        return s


    def atv13(self, n: int):
        s = []
        c = 1
        while True:
            denominador = c
            s.append(float(f'{1/denominador:.2f}'))
            if c==n:
                break
            c+=1
        return sum(s)


    def atv14(self, n: int):
        def fat(i):
            f = 1
            for c in range(i, 0, -1):
                f*=c
            return f
        s = []
        c = 1
        while True:
            denominador = c
            s.append(1/fat(denominador))
            if c==n:
                break
            c+=1
        return sum(s)


    def atv15(self, n: int):
        s = []
        c = 1
        while True:    
            numerador = (c**2)+1
            denominador = c+3
            s.append(float(f'{numerador/denominador:.2f}'))
            if c==n:
                break
            c+=1
        return sum(s)


def main():
    i = revisao_funcoes()
    while True:
        limpar()
        user = i.home()
        if user == "1":
            x = int(input("Digite um número inteiro: "))
            print(f"O número digitado é {'PAR' if i.atv1(x) else 'IMPAR'}.")
            input("\nPressione enter para voltar.")

        elif user == "2":
            raio = float(input("Raio: "))
            opc = int(input("Calcular:\n[ 1 ] ÁREA\n[ 2 ] PERÍMETRO\n>> "))
            print(f"{'ÁREA: 'if opc==1 else 'PERÍMETRO: '}{i.atv2(raio, opc)}")
            input("\nPressione enter para voltar.")

        elif user == "3":
            f = float(input("Temperatura °F: "))
            print(f"A temperatura {f}°F convertida para Celsius é de {i.atv3(f):.2f}°C")
            input("\nPressione enter para voltar.")                  
        
        elif user == "4":
            n1 = float(input("Digite a 1° nota: "))
            n2 = float(input("Digite a 2° nota: "))
            print(i.atv4(n1, n2))
            input("\nPressione enter para voltar.")

        elif user == "5":
            a = float(input("Altura: "))
            s = int(input("Sexo[1-F, 2-M]: "))
            print(f"Seu peso ideal é de {i.atv5(a, s):.2f}")
            input("\nPressione enter para voltar.")

        elif user == "6":
            l = int(input("Número de lados de um polígono regular [3, 4 ou 5]: "))
            m = float(input("Medida do lado: "))
            print(i.atv6(l, m))
            input("\nPressione enter para voltar.")

        elif user == "7":
            n = int(input("Digite um número inteiro: "))
            print(i.atv7(n))
            input("\nPressione enter para voltar.")

        elif user == "8":
            c = "S"
            while c == "S":
                num = input("Número: ")
                print(f"Cubo: {int(num)*int(num)*int(num)}")
                c = input("Continuar?[S/N]").upper().strip()
                print(i.atv8(c))

        elif user == "9":
            n1 = int(input("1° número: "))
            n2 = int(input("2° número: "))
            print(f"A soma do intervalo {n1} à {n2} é {i.atv9(n1, n2)}")
            input("\nPressione enter para voltar.")

        elif user == "10":
            list_a = input("Digite a PRIMEIRA sequência de números separada por espaço\n>>> ").strip()
            list_b = input("\nDigite a SEGUNDA sequência de números separada por espaço\n>>> ").strip()
            a_list = [int(num) for num in list_a.split()]
            b_list = [int(num) for num in list_b.split()]
            print(i.atv10(a_list, b_list))
            input("\nPressione enter para voltar.")

        elif user == "11":
          n = int(input("Digite um número: "))
          print(f"O número {n} é divisível por:\n>> {i.atv11(n)}")
          input("\nPressione enter para voltar.")

        elif user == "12":
            n = int(input("Digite um número: "))
            print(f"A somatório do número {n} é:\n>> {i.atv12(n)}")
            input("\nPressione enter para voltar.")

        elif user == "13":
            n = int(input("Digite um número: "))
            print(f"O número {n} na expressão S = 1 + 1⁄2 + 1/3 + 1⁄4 + 1/5 + 1/N:\n>> {i.atv13(n):.2f}")
            input("\nPressione enter para voltar.")
        
        elif user == "14":
            n = int(input("Digite um número: "))
            print(f"O número {n} na expressão S = 1 + 1/1! + 1⁄2! + 1/3! + 1 /N!:\n>> {i.atv14(n):.2f}")
            input("\nPressione enter para voltar.")

        elif user == "15":
            n = int(input("Digite um número: "))
            print(f"O número {n} na expressão S = 2/4 + 5/5 + 10/6 + 17/7 + 26/8 + ... +(t^2+1)/(t+3):\n>> {i.atv15(n):.2f}")
            input("\nPressione enter para voltar.")

        else:
            break


if __name__ == '__main__':
    main()
