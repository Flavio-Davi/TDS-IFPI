from os import system
from time import sleep
from datetime import datetime
import string


class Cofre_Eletronico:
    def __init__(self):
        self.estado = False
        self.tentativas = 3
        self.listClientes = {}
        self.historic = {"DATA": [], "HORA": [], "ACESSO": []}
        self.cor = {"red": "\033[1;31m", "yellow": "\033[1;32m", "green": "\033[1;33m", "end": "\033[0m"}


    def primeiro_acesso(self):
        print(" CRIAR USUARIO E SENHA ".center(50, "#"))

        user = input("Digite seu nome de usuario: ")

        while True:
            self.listClientes[f"{user}"] = input("Digite sua senha: ")
            confirm_senha = input("Confirme sua senha: ")

            if self.listClientes[f"{user}"] != confirm_senha:
                print(">>> Senhas diferentes.")
                sleep(1)
                system("clear")
                continue
            else:
                time = 3
                while time > 0:
                    system("clear")
                    print(self.cor["green"] + "\n>>> Usuario e senha criado com sucesso. Você será recirecionado para o menu em instantes.")
                    print(f"{time}")
                    sleep(1) 
                    time-=1
                break


    def alterar_senha(self):
        cliente = input(self.cor["yellow"] + "Digite seu nome de usuário: ")
        senhaValida = string.punctuation
        senhaValida1 = string.digits
        
        if cliente in self.listClientes:
            while True:
                system("clear")
                print(" ALTERAR SENHA ".center(50, "#"))
                senha = input("Digite sua nova senha: ")
                confirm_senha = input("Confirme a senha: ")

                for c in range(senha):
                    if senha[c] not in senhaValida or senha[c] not in senhaValida1:
                        print(self.cor["red"]+">>> Adicione pelo menos um numero e um caractere em sua senha.")
                        sleep(1)
                        break
                if senha != confirm_senha:
                    print(self.cor["red"]+">>> Senhas diferente.")
                    sleep(1)
                    continue                            
                else:
                    self.listClientes[f"{cliente}"] = senha
                    print(">>> Senha alterada com sucesso. Pressione enter para voltar.")
                    input() 
                    break
        else:
            time = 2
            while time < 0:
                system("clear")
                print("Cliente não identificado, você retornará ao menu em instantes!")
                sleep(1) 
                time-=1


    def validar_acesso(self, usuario, senha):
        if usuario and senha in self.listClientes:
            return True
        else: 
            return False


    def abrir_fechar(self):
        userTentativas = 0
        while True:
            system("clear")
            print(" ABRIR COFRE ".center(50, "#"))
            print(f"TENTATIVAS [{userTentativas}/3]\n")
            usuario = input("Usuario: ")
            senha = input("Senha: ") 
            validar = self.validar_acesso(usuario, senha)


            if userTentativas > 2:
                self.historic["DATA"].append(datetime.now().strftime("%d/%m/%Y"))
                self.historic["HORA"].append(datetime.now().strftime("%H:%M:%S"))
                self.historic["ACESSO"].append("NEGADO")
                input("Redefina sua senha, pressione enter para voltar ao menu principal")
                break 

            elif not validar:
                self.historic["DATA"].append(datetime.now().strftime("%d/%m/%Y"))
                self.historic["HORA"].append(datetime.now().strftime("%H:%M:%S"))
                self.historic["ACESSO"].append("NEGADO")

                userTentativas += 1
                print(self.cor["red"] + ">>> SENHA INCORRETA" + self.cor["end"])
                sleep(0.5)
                system("clear")
            else:
                self.historic["DATA"].append(datetime.now().strftime("%d/%m/%Y"))
                self.historic["HORA"].append(datetime.now().strftime("%H:%M:%S"))
                self.historic["ACESSO"].append("LIBERADO")

                print(f"\nBem vindo de volta!\nSeu cofre agora está aberto!")
                input("Você não tem nada em seu cofre.")
                break


    def historico(self):
        print(" HISTÓRICO ".center(50, "#"))
        print(f"\n|    DATA    |   HORA   |   ACESSOS")

        for c in range(len(self.historic["DATA"])):
            print(f"| {self.historic['DATA'][c]} | {self.historic['HORA'][c]} | {self.historic['ACESSO'][c]}")

        input("\n>>> Pressione enter para voltar")



if __name__ == "__main__":
    cofre = Cofre_Eletronico()

    while True:
        system("clear")
        print("\033[1;35m" + " NuCofres ".center(50, "#"))
        menu = input("""\n[ 1 ] - Criar conta
[ 2 ] - Histório
[ 3 ] - Alterar senha
[ 4 ] - Abrir Cofre
[ 5 ] - Sair
\n>>> """)
        
        if menu == "1":
            system("clear")
            cofre.primeiro_acesso()
        elif menu == "2":
            system("clear")
            cofre.historico()
        elif menu == "3":
            system("clear")
            cofre.alterar_senha()
        elif menu == "4":
            system("clear")
            cofre.abrir_fechar()
        elif menu == "5":
            system("clear")
            print("\n>>> Programa finalizado, volte sempre.")
            break
        else:
            system("clear")
            continue
