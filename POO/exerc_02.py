# Implementar uma classe Veiculo que represente o registro de um veículo em um sistema de
# controle de veículos. A atividade deve explorar a criação de construtores, atributos
# obrigatórios e opcionais, o uso de métodos para exibir e atualizar as informações do veículo, e
# incluir funcionalidades como cálculo de depreciação, verificação de validade de placae venda
# com atualização do proprietário.
import string
from datetime import datetime

class Veiculo:
    def __init__(self, chassi, marca: str, modelo: str, ano: int, cor: str):
        self.chassi = chassi
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.placa = "SEM PLACA"
        self.proprietario = "Não especificado"
        self.quilometragem = 0
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
        modelo = ["ACB-1234", "ABC-1A23"]
        letras = string.ascii_letters
        numeros = string.digits

        valida = False

        # Verifica 1° parte
        for c in range(len(new_placa)):
            if new_placa[c] in letras and c<3: 
                valida = True
            else:
                valida = False
        
        # Verifica os numeros
        for c in range(len(new_placa[3::])):
            if new_placa[c] in letras and c<8: 
                valida = True
            else:
                valida = False

        return valida


    def calcular_depriacao(self):
        ano_atual = datetime.now().year
        tempo = ano_atual-self.ano
        
        # M = C*(1 + i)t
        depreciacao = self.valor*(1+5)**tempo
        
        return depreciacao
        

    def atualizar_quilometragem(self):
        pass


    def atualizar_propietario(self):
        pass

    
    def vender(self):
        pass


if __name__ == '__main__':
    v = Veiculo(1, "Toyota", "Corola", 2001, "Amarelo")
    print(v.calcular_depriacao())
