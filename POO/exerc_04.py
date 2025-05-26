from os import name
from os import system
from time import sleep
from datetime import datetime

def limpar():
    return system("cls") if name == "nt" else system("clear")


class Boleto:
    def __init__(self):
        self.cor = {"vermelho": "\033[1;31m", "verde": "\033[1;32m", "amarelo": "\033[1;33m", 
                    "azul": "\033[1;34m", "roxo": "\033[1;35m", "cyano": "\033[1;36m"}
        self.data_base = {}
        self.id_boleto = 1
        self.data_atual = datetime.today().strftime("%d/%m/%Y")


    def menu(self):
        valido = ["1", "2", "3", "4"]
        while True:
            limpar()
            user = input(self.cor["amarelo"]+"""
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
                print(self.cor["vermelho"]+"\t\tERROR: Opção inválida, verifique e tente novamente.")
                sleep(1)
                continue
            else: break

        return user
    

    def criar(self, nome: str, data_emissao: datetime, data_venc: datetime):
        data = []
        for key, value in self.data_base.items():
            if self.id_boleto == key:
                self.id_boleto += 1

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


if __name__ == '__main__':
    i = Boleto()
    
    while True:
        iniciar = i.menu()

        if iniciar == "1":
            nome = input("Nome do devedor: ")
            data_emissao = input("Data da emissão: ")
            data_venc = input("Data de vencimento: ")

            print(i.criar(nome, data_emissao, data_venc))
            sleep(2)
        if iniciar == "2":
            i.consulta()
        if iniciar == "3":
            pass
        if iniciar == "4":
            pass
        if iniciar == "5":
            limpar()
            print(">>> Programa encerrado.")
            break
