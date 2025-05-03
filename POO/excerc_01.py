from os import system
from os import name
from datetime import datetime


def limpar():
    return system("cls") if name=="nt" else system("clear")

class ArCondicionado:
    def __init__(self, modelo: str, marca: str, potencia: int, estado: bool = False):
        self.modelo = modelo
        self.marca = marca
        self.potencia = potencia
        self.estado = estado
        self.temp_atual = int(24)
        self.modo = "RESFRIAR"
        self.timer = None
        self.velocidade = "MÉDIA"

    
    def __str__(self):
        limpar()
        return f"""    ########################################
            INFORMAÇÕES DO APARELHO
    ########################################\n
    MODELO........................{self.modelo}
    MARCA.........................{self.marca}
    POTENCIA......................{self.potencia}
    ESTADO........................{self.estado}
    TEMPERATURA...................{self.temp_atual}
    MODO..........................{self.modo}
    DESLIGAR:.....................Em {self.timer} 
    VELOCIDADE....................{self.velocidade}"""


    def ligar(self):
        limpar()
        if self.estado == True:
            self.estado = False
            return ">> Ar condicionado desligado com sucesso."
        else:
            self.estado = True 
            return ">> Ar condicionado ligado com sucesso."


    def alterar_temp(self, nova_temp: float):
        limpar()
        if nova_temp >=17 and nova_temp <= 26:
            self.temp_atual = nova_temp
            return f">> Temperatura do arcondicionado alterada para {nova_temp}°C."
        else:
            return f">> A temperatura de {nova_temp} está fora do escopo do arcondicionado,\ninsira uma temperatura válida entre 17°C e 26°C."


    def alterar_modo(self, novo_modo: str):
        limpar()
        modos = ["RESFRIAR", "AUTOMÁTICO", "AUTOMATICO", "VENTILAR", "AQUECER"]

        if self.estado==True and novo_modo.upper() in modos:
            self.modo = novo_modo.upper()
            return f">> Modo alterado para {novo_modo}"
        else:
            if novo_modo.upper() not in modos:
                return f">> O modo {novo_modo} é inválido, por favor insira um modo válido:\n> {"\n> ".join(map(str, modos))}"
            else:
                return ">> Ligue o arcondicionado antes de realizar qualquer operação."


    def programar_timer(self, time_sleep):
        limpar()
        try:
            now = datetime.now().strftime("%H:%M")
            
            time_now = datetime.strptime(now, "%H:%M")
            user = datetime.strptime(time_sleep, "%H:%M")
            self.desligar = user-time_now
            self.sleep = True
            self.timer = time_sleep
            return f"Aparalho programado para desligar em {f"{str(self.desligar) if len(str(self.desligar))<=7 else str(self.desligar)[10::]}"}"
            
        except ValueError:
            self.sleep = False
            return "\n>> Valor digitado inválido, digite apenas números em hora e minutos."


    def reset_timer(self):
        limpar()
        self.timer = None
        return ">> Tempo de desligamento automático zerado."


    def alterar_velocidade(self, nova_velocidade: str):
        limpar()
        velocidades = ["BAIXA", "MÉDIA", "MEDIA", "ALTA"]

        if self.estado==True and self.modo not in ["AUTOMÁTICO", "AUTOMATICO"] and nova_velocidade.upper() in velocidades:
            return f">> Velocidade do arcondionado alterada para {nova_velocidade}"
        elif self.estado==False:
            return ">> Ligue o arcondicionado antes de realizar qualquer operação."
        elif self.modo=="AUTOMÁTICO" or self.modo=="AUTOMATICO":
            return ">> Arcondionado no modo automático, altere o modo para alterar a velocidade."


    def reset_config(self):
        limpar()
        self.temp_atual = int(24)
        self.modo = "RESFRIAR"
        self.timer = None
        self.velocidade = "MÉDIA"
        return ">> Configurações resetadas."


if __name__ == '__main__':
    t = ArCondicionado("Split", "Electrolux", 7000)
    t.ligar()
    
