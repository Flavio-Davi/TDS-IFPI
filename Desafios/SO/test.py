# Criar arquivo "dados.txt", caso não exista, se existir criar.
from time import sleep
import os

class exercSO():
    def __init__(self):
        self.executar()



    def home(self):
        self.cores = {"vermelho": "\033[1;31m", "verde": "\033[1;32m", "amarelo": "\033[1;33m", "azul": "\033[1;34m"}
        
        while True:
            print(self.cores["amarelo"]+" MENU ".center(40, "#"))
            user = int(input("""\n[ 1 ] - Adicionar novos nomes
[ 2 ] - Exibir nomes 
[ 3 ] - Pesquisar nome (Informar o n° da linha)
[ 4 ] - Editar item
[ 5 ] - Sair
\n➥ """))

            if user>5 or user<0:
                print(self.cores["vermelho"] + "ERROR: opção inválida, digite uma opção válida.")
                sleep(1)
                os.system("clear")
                continue
            else:    
                break             
        return user
        

    def adicionar(self): 
        dados = open("dados.txt", "a")
        dado = input("Digite o nome: ")
        dados.write(f"\n{dado}")    
        dados.close()

        print(self.cores["verde"]+f"O nome {dado} foi adicionado aos dados.")
        sleep(1)
        os.system("clear")
        


    def exibir(self):
        os.system("clear")
        dados = open("dados.txt", "r")
        print(" DADOS ".center(40, "-")) 
        leitura = print(f"{"\n".join(map(str, dados.readlines()))}")
        input("\nPressione qualquer tecla para voltar ao menu.")
        dados.close()
        os.system("clear")

        return leitura


    def pesquisar(self, nome):
        dados = open("dados.txt", "r").readlines()
        linha = 0

        for dado in dados:
            linha += 1
            if nome == dado.strip("\n"):
                return linha 


    def editar(self, linha):
        new_nome = input("Digite o novo nome: ")
        
        dados = open("dados.txt", "w")
        linhas = dados.readlines()
        linhas[linha - 1] = new_nome + "\n"
        dados.writelines(linhas)
        print(self.cores["verde"]+"Nome editado com sucesso!") 


    def executar(self):
        while True:
            user = self.home()
            if user == 1:
                self.adicionar()
            
            if user == 2:
                self.exibir()
            
            if user == 3:
                nome = input(self.cores["azul"]+"Digite o nome que deseja pesquisar: ")
                print(f"A linha do nome {nome} é a {self.pesquisar(nome)}.")
                os.system(1)

            if user == 4:
                nome = input()
                
            elif user == 5:
                print("Até logo!")
                break


exercSO()