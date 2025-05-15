# Implementar uma classe Veiculo que represente o registro de um veículo em um sistema de
# controle de veículos. A atividade deve explorar a criação de construtores, atributos
# obrigatórios e opcionais, o uso de métodos para exibir e atualizar as informações do veículo, e
# incluir funcionalidades como cálculo de depreciação, verificação de validade de placae venda
# com atualização do proprietário.
from os import system
from os import name
import string
from re import fullmatch
from datetime import datetime

def limpar():
    return system("cls") if name=="nt" else system("clear")


class Veiculo:
    def __init__(self, chassi, marca: str, modelo: str, ano: int, cor: str):
        self.chassi = chassi
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.placa = "SEM PLACA"
        self.proprietario = "Não especificado"
        self.quilometragem = 0.0
        self.valor = 1000.0
    

    def __str__(self):
        info = f"""------------------------------
    I N F O R M A Ç Õ E S    
------------------------------

CHASSI......................{self.chassi}
MARCA.......................{self.marca}
MODELO......................{self.modelo}
ANO.........................{self.ano}
COR.........................{self.cor}
PLACA.......................{self.placa}
PROPIETÁRIO.................{self.proprietario}
QUILOMETRAGEM...............{self.quilometragem}km
VALOR.......................R${self.valor}
"""

        return info


    def validar_placa(self, new_placa):
        valido = r"^[A-Z]{3}-[A-Z0-9]{4}$"

        return bool(fullmatch(valido, new_placa))


    def calcular_depriacao(self):
        ano_atual = datetime.now().year
        tempo = ano_atual - self.ano
        taxa = 0.05
        valor_final = self.valor * (1 - taxa) ** tempo
        valor_minimo = self.valor * 0.10

        if valor_final < valor_minimo:
            valor_final = valor_minimo
        

    def atualizar_quilometragem(self, new_km: float):
        if new_km > self.quilometragem:
            self.quilometragem += new_km
            return f"QUILOMETRAGEM ATUALIZA\n>>> {self.quilometragem}km"
        else:
            return f"Quilometragem inserida inferior ao valor atual de {self.quilometragem}km, insira um valor válido, maior que a quilometragem atual para atualização."


    def atualizar_propietario(self, new_property):
        self.proprietario = new_property
        return f"Propietário atualizado para Sr.(a) {self.proprietario}"

    
    def vender(self, value, name_property):
        valor_mercado = self.valor * (1 - 0.05) ** (datetime.now().year - self.ano)
        valor_minimo = self.valor * 0.10

        if valor_mercado < valor_minimo:
             valor_mercado = valor_minimo
 
        self.proprietario = name_property

        
        return "Veículo vendido acima do valor de mercado." if value > valor_mercado else "Veículo vendido abaixo do valor de mercado."


if __name__ == '__main__':
    v = Veiculo(1, "Toyota", "Corola", 2001, "Amarelo")
