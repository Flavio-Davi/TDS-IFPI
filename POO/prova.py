# Ludimila Andrade Maciel & Flávio Davi da Silva Alves

import datetime
import json
from os import system, name
from time import sleep

cor = {
    "vermelho": "\033[1;31m", "verde": "\033[1;32m", "amarelo": "\033[1;33m",
    "azul": "\033[1;34m", "roxo": "\033[1;35m", "cyano": "\033[1;36m"
}

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
        [ 1 ] - Reservar quarto
        [ 2 ] - Cancelar reserva
        [ 3 ] - Alterar reserva
        [ 4 ] - Fazer check-in
        [ 5 ] - Sair
                
            -> """)
        if user not in valido:
            print(cor["vermelho"]+"\t\tERROR: Opção inválida.")
            sleep(1)
            continue
        else:
            break
    return user

def pedir_data(msg):
    while True:
        try:
            limpar()
            print(msg.center(50, "#"))
            d = int(input("dia: "))
            m = int(input("mês: "))
            a = int(input("ano: "))
            return datetime.date(a, m, d)
        except:
            print("Data inválida.")
            sleep(1)

class Reserva:
    def __init__(self):
        self._id = 0
        self._tipo_quarto = {"SIMPLES": 150.0, "DUPLO": 250.0, "LUXO": 400.0}
        self.reservas = {}
        self.carregar()

    @property
    def tipo_quarto(self):
        return self._tipo_quarto

    def salvar(self):
        with open("reservas.json", "w") as f:
            json.dump({"id": self._id, "dados": self.reservas}, f, default=str)

    def carregar(self):
        try:
            with open("reservas.json", "r") as f:
                data = json.load(f)
                self._id = data["id"]
                for k, v in data["dados"].items():
                    v[2] = datetime.datetime.strptime(v[2], "%Y-%m-%d").date()
                    v[3] = datetime.datetime.strptime(v[3], "%Y-%m-%d").date()
                    self.reservas[int(k)] = v
        except:
            self._id = 0
            self.reservas = {}

    def reservar(self, nome, tipo_qt, data_checkIN, data_checkOUT):
        self._id += 1
        qtd_diaria = (data_checkOUT - data_checkIN).days
        valor_total = qtd_diaria * self.tipo_quarto[tipo_qt]
        self.reservas[self._id] = [nome, tipo_qt, data_checkIN, data_checkOUT, qtd_diaria, "ATIVA", valor_total]
        self.salvar()

    def visualizar(self):
        if not self.reservas:
            print("Nenhuma reserva encontrada.")
            return
        for k, v in self.reservas.items():
            print(f"ID: {k} | Nome: {v[0]} | Quarto: {v[1]} | Check-in: {v[2]} | Check-out: {v[3]} | Diárias: {v[4]} | Total: R${v[6]:.2f} | Status: {v[5]}")

    def cancelar(self, reserva_id):
        if reserva_id in self.reservas and self.reservas[reserva_id][5] == "ATIVA":
            self.reservas[reserva_id][5] = "CANCELADA"
            self.salvar()
            return True
        return False

    def alterar(self, reserva_id, novo_checkIN, novo_checkOUT):
        if reserva_id in self.reservas and self.reservas[reserva_id][5] == "ATIVA":
            qtd_diaria = (novo_checkOUT - novo_checkIN).days
            tipo_qt = self.reservas[reserva_id][1]
            valor_total = qtd_diaria * self.tipo_quarto[tipo_qt]
            self.reservas[reserva_id][2] = novo_checkIN
            self.reservas[reserva_id][3] = novo_checkOUT
            self.reservas[reserva_id][4] = qtd_diaria
            self.reservas[reserva_id][6] = valor_total
            self.salvar()
            return True
        return False

    def checkin(self, reserva_id):
        if reserva_id in self.reservas and self.reservas[reserva_id][5] == "ATIVA":
            self.reservas[reserva_id][5] = "CONCLUIDA"
            self.salvar()
            return True
        return False

if __name__ == '__main__':
    i = Reserva()
    while True:
        user = menu()
        hoje = datetime.date.today()

        if user == "1":
            nome = input("Digite seu nome: ")
            while True:
                limpar()
                print(" ESCOLHA DE QUARTO ".center(50, "#"))
                print("\n[ 1 ] - SIMPLES\n[ 2 ] - DUPLO\n[ 3 ] - LUXO")
                tipo_qt = input(">> ")
                if tipo_qt in ["1", "2", "3"]:
                    tipo_qt = ["SIMPLES", "DUPLO", "LUXO"][int(tipo_qt) - 1]
                    break

            data_checkIN = pedir_data(" DATA DE CHECK-IN ")
            if data_checkIN < hoje:
                print("Data de check-in inválida.")
                sleep(2)
                continue

            data_checkOUT = pedir_data(" DATA DE CHECK-OUT ")
            if data_checkOUT <= data_checkIN:
                print("Data de check-out inválida.")
                sleep(2)
                continue

            i.reservar(nome, tipo_qt, data_checkIN, data_checkOUT)
            print("Reserva realizada com sucesso.")
            sleep(2)

        elif user == "2":
            limpar()
            i.visualizar()
            try:
                reserva_id = int(input("ID da reserva para cancelar: "))
                if i.cancelar(reserva_id):
                    print("Reserva cancelada.")
                else:
                    print("Não foi possível cancelar.")
            except:
                print("ID inválido.")
            sleep(2)

        elif user == "3":
            limpar()
            i.visualizar()
            try:
                reserva_id = int(input("ID da reserva para alterar: "))
                novo_checkIN = pedir_data(" NOVA DATA DE CHECK-IN ")
                novo_checkOUT = pedir_data(" NOVA DATA DE CHECK-OUT ")
                if novo_checkOUT <= novo_checkIN or novo_checkIN < hoje:
                    print("Datas inválidas.")
                elif i.alterar(reserva_id, novo_checkIN, novo_checkOUT):
                    print("Reserva alterada.")
                else:
                    print("Não foi possível alterar.")
            except:
                print("Erro na alteração.")
            sleep(2)

        elif user == "4":
            limpar()
            i.visualizar()
            try:
                reserva_id = int(input("ID da reserva para check-in: "))
                if i.checkin(reserva_id):
                    print("Check-in realizado.")
                else:
                    print("Não foi possível realizar check-in.")
            except:
                print("ID inválido.")
            sleep(2)

        elif user == "5":
            print("Saindo...")
            break
