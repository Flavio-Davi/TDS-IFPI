from os import system
from time import sleep

class Cofre_Eletronico:
    def __init__(self):
        self.estado = False
        self.tentativas = 3
        self.listClientes = {}
        self.cor = {"red": "\033[1;31m", "yellow": "\033[1;32m", "green": "\033[1;33m"}


    def primeiro_acesso(self):
        print(" CRIAR USUARIO E SENHA ".center(50, "#"))

        user = input("Digite seu nome de usuario: ")

        while True:
            self.listClientes[f"{user}"] = input("Digite sua senha: ")
            system("clear")
            confirm_senha = input("Confirme sua senha: ")

            if self.listClientes[f"{user}"] != confirm_senha:
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
        
        if cliente in self.listClientes:
            while True:
                system("clear")
                print(" ALTERAR SENHA ".center(50, "#"))
                senha = input("Digite sua nova senha: ")
                system("clear")
                print(" ALTERAR SENHA ".center(50, "#"))
                confirm_senha = input("Confirme a senha: ")

                if senha != confirm_senha:
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
            

    def abrir_fechar(self):
        userTentativas = 0
        while True:
            system("clear")
            print(" ABRIR COFRE ".center(50, "#"))
            print(f"TENTATIVAS [{userTentativas}/3]\n")
            usuario = input("Usuario: ")
            senha = input("Senha: ") 
            senha_correta = self.listClientes[f"{usuario}"]


            if userTentativas == 3:
                input("Redefina sua senha, pressione enter para voltar ao menu principal")
                break 
            elif senha != senha_correta:
                userTentativas += 1
                print(self.cor["red"] + ">>> SENHA INCORRETA")
                sleep(0.5)
                system("clear")
            else:
                print(f"\nBem vindo de volta!\nSeu cofre agora está aberto!")
                input("Você não tem nada em seu cofre.")
                break


if __name__ == "__main__":
    cofre = Cofre_Eletronico()

    while True:
        system("clear")
        print("\033[1;35m" + " NuCofres ".center(50, "#"))
        menu = input("""\n[ 1 ] - Primeiro acesso
[ 2 ] - Alterar senha
[ 3 ] - Abrir Cofre
[ 4 ] - Sair
\n>>> """)
        
        if menu == "1":
            system("clear")
            cofre.primeiro_acesso()
        elif menu == "2":
            system("clear")
            cofre.alterar_senha()
        elif menu == "3":
            system("clear")
            cofre.abrir_fechar()
        elif menu == "4":
            system("clear")
            print("\n>>> Programa finalizado, volte sempre.")
            break
        else:
            system("clear")
            continue

