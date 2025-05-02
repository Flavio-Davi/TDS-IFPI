# Implementar a classe ArCondicionado, explorando criação de construtores, atributos
# obrigatórios e opcionais, métodos de exibição, atualização e manipulação de estados do aparelho.
from datetime import datetime, timedelta


class ArCondicionado:
    def __init__(self, modelo: str, marca: str, potencia: int, estado: bool = False):
        self.modelo = modelo
        self.marca = marca
        self.potencia = potencia
        self.estado = estado  
        

    def __str__(self):
        return f"""############################
    ESPECIFICAÇÕES ATUAL
############################

MODELO: {self.modelo}
MARCA: {self.marca}
POTÊNCIA: {self.potencia}
ESTADO: {self.estado}
---------------------------
TEMPERATURAL ATUAL: {self.atual}°C
MODO ATUAL: {self.modo_atual}
DESLIGAR AUTOMATICAMENTE: {'Não programado' if self.sleep == False else f'Programado para desligar em {self.desligar}'}"""


    def temperatura(self, atual: int = 24):
            self.atual = atual
            return f">> Temperatura programada para {self.atual}°C"

    
    def modo(self, mod="RESFRIAR"):
        modos = ["RESFRIAR", "AQUECER", "VENTILAR"]
        self.modo_atual = mod

        if mod.upper() in modos and self.estado==True:
            return f">>> Modo alterado para {mod.upper()}."
        elif self.estado==False:
            return ">>> O aparelho está desligado, ligue para selecionar um modo operante."
        else:
            return f"Modo selecionado não compatível, selecione um modo válido.\n>> {"\n>> ".join(map(str, modos))}"


    def timer(self, hora, min):
        try:
            self.sleep = True
            user_time = f"{hora}:{min}"
            now = datetime.now().strftime("%H:%M")
            
            time_now = datetime.strptime(now, "%H:%M")
            user = datetime.strptime(user_time, "%H:%M")
            self.desligar = user-time_now
            
            return f"Aparalho programado para desligar em {f"{str(self.desligar) if len(str(self.desligar))<=7 else str(self.desligar)[10::]}"}"
    
        except ValueError:
            self.sleep = False
            return "\n>> Valor digitado inválido, digite apenas números em hora e minutos."


if __name__ == '__main__':
    t = ArCondicionado("t", "t", 25, True)
    print(t.__str__())
