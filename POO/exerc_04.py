from re import search
from os import name
from os import system
from time import sleep
from datetime import datetime

cor = {"vermelho": "\033[1;31m", "verde": "\033[1;32m", "amarelo": "\033[1;33m", 
        "azul": "\033[1;34m", "roxo": "\033[1;35m", "cyano": "\033[1;36m"}

def limpar():
    return system("cls") if name == "nt" else system("clear")


def menu():
        valido = ["1", "2", "3", "4", "5"]
        while True:
            limpar()
            user = input(cor["amarelo"]+"""
            -----------------------------
                       M E N U
            -----------------------------
            [ 1 ] - Cadastrar novo boleto 
            [ 2 ] - Visualizar boletos
            [ 3 ] - Excluir Boleto
            [ 4 ] - Pagar boleto
            [ 5 ] - Encerrar programa
                    
                -> """)
            
            if user not in valido:
                print(cor["vermelho"]+"\t\tERROR: Opção inválida, verifique e tente novamente.")
                sleep(1)
                continue
            else: break

        return user


class Boleto:
    def __init__(self):
        self.data_base = {}
        self.id_boleto = 0
        self.STATUS = ["EM ABERTO", "PAGO", "VENCIDO", "CANCELADO"]
        self.data_atual = datetime.today().strftime("%d/%m/%Y")


    def criar(self, nome: str, data_emissao: datetime, data_venc: datetime):
        data = []
        self.id_boleto += 1

        data.append(self.STATUS[0])
        data.append(nome)
        data.append(data_emissao)
        data.append(data_venc)
        self.data_base[self.id_boleto] = data

        return f"\n>>> Boleto número {self.id_boleto} criado com sucesso."


    def consulta(self):
        print("ID boleto\t\tInformações")
        for key, value in self.data_base.items():
            print(f"{key:<20}{value}")
        
        return input("\nPressione enter para voltar.")


    def excluir(self, id_boleto: int):
        verificar = False
        for key, value in self.data_base.items():
            if key == id_boleto:
                verificar = True
        if verificar:
            self.data_base.pop(id_boleto)
            return f"\n>>> Boleto de ID {id_boleto}, excluido com sucesso."
        else:
            return f"\nBoleto de ID {id_boleto} não localizado, verifique e tente novamente."


    def pagar(self, id_boleto):
        verificar = False
        for key, value in self.data_base.items():
            if key == id_boleto:
                verificar = True
        if verificar == True:
            if search("EM ABERTO", self.data_base[id_boleto][0]):
                self.data_base[id_boleto][0] = "PAGO"
                return ">>> Boleto pago com sucesso."
            else:
                return f">>> O boleto de ID {id_boleto}, não está com status EM ABERTO.\nContatar o emissor."
        else:
            return ">>> ID digita não encontrado, verifique e tente novamente."


if __name__ == '__main__':
    i = Boleto()
    
    while True:
        iniciar = menu()

        if iniciar == "1":
            nome = input("Nome do devedor: ")
            data_emissao = input("Data da emissão: ")
            data_venc = input("Data de vencimento: ")

            print(cor["verde"]+i.criar(nome, data_emissao, data_venc))
            sleep(2)
        if iniciar == "2":
            i.consulta()
        if iniciar == "3":
            id_boleto = int(input("Digite o ID do boleto que deseja excluir: "))
            print(i.excluir(id_boleto))
            sleep(1)
        if iniciar == "4":
            id_pagar = int(input("Digite o ID do boleto que deseja pagar: "))
            print(i.pagar(id_pagar))
            sleep(2)
        if iniciar == "5":
            limpar()
            print(">>> Programa encerrado.")
            break
