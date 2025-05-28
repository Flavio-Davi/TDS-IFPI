from re import search
from os import name
from os import system
from time import sleep
import datetime 

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
        self._id_boleto = 0
        self.STATUS = ["EM ABERTO", "PAGO", "VENCIDO", "CANCELADO"]
        self.data_atual = datetime.datetime.strptime(datetime.datetime.today().strftime("%d/%m/%Y"), "%d/%m/%Y").date

    @property
    def id_boleto(self):
        return self._id_boleto


    def valor_atual(self, id_boleto: int):
        """Desconto de 5% se pago até 3 dias antes do vencimento.
        Multa de 2% + juros de 0,03% ao dia se pago após o vencimento."""

        if id_boleto not in self.data_base:
            raise ValueError(">>> ID não encontrado, verificar e tentar novamente.")
        
        data_venc = self.data_base[id_boleto][4]
        if isinstance(data_venc, str):
            data_venc = datetime.datetime.strptime(data_venc, "%d/%m/%Y").date()
        
        return (data_venc-self.data_atual).days


    def criar(self, nome: str, valor: float, data_emissao: datetime, data_venc: datetime):
        data = []
        self._id_boleto += 1

        data.append(self.STATUS[0])
        data.append(nome)
        data.append(valor)
        data.append(data_emissao)
        data.append(data_venc)
        data.append("")
        self.data_base[self.id_boleto] = data

        return f"\n>>> Boleto número {self.id_boleto} criado com sucesso."


    def consulta(self):
        print(cor["azul"]+f"{'ID':<10}{'STATUS':<13}{'NOME':<16}{'VALOR R$':<19}{'DATA EMISSÃO':<22}{'DATA VENCIMENTO':<25}{'REGISTRO DE PAGAMENTO':<28}")
        for key, value in self.data_base.items():
            print(cor["cyano"]+f"{key:<10}{value[0]:<13}{value[1]:<16}{value[2]:<19}{value[3]:<22}{value[4]:<25}{value[5]:<28}")
        
        return input("\nPressione enter para voltar.")


    def cancelar(self, id_boleto: int):
        verificar = False
        for key, value in self.data_base.items():
            if key == id_boleto:
                verificar = True
        if verificar:
            self.data_base[id_boleto][0] = "CANCELADO"
            return f"\n>>> Boleto de ID {id_boleto}, cancelado com sucesso."
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
                self.data_base[id_boleto][5] = self.data_atual
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
            valor = input("Valor do boleto: R$")
            data_emissao = input("Data da emissão: ")
            data_venc = input("Data de vencimento: ")

            print(cor["verde"]+i.criar(nome, valor, data_emissao, data_venc))
            sleep(2)

        if iniciar == "2":
            i.consulta()

        if iniciar == "3":
            id_boleto = int(input("Digite o ID do boleto que deseja excluir: "))
            print(i.cancelar(id_boleto))
            sleep(1)
        
        if iniciar == "4":
            id_pagar = int(input("Digite o ID do boleto que deseja pagar: "))
            print(i.valor_atual(id_pagar))
            print(i.pagar(id_pagar))
            sleep(2)
        
        if iniciar == "5":
            limpar()
            print(">>> Programa encerrado.")
            break
