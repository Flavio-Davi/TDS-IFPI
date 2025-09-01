from query import Querie
from datetime import date
from db_config import Conexao
from time import sleep
import os


class Escola:
    def __init__(self):
        self.cnx = Conexao()
        self.q = Querie()


    def criar_professor(self, p_nome: str, s_nome: str, matricula: str, data_nasc: date, email: str):
        return self.cnx.execute_query_update(self.q.create_teacher(), (p_nome, s_nome, matricula, data_nasc, email))


    def visualizar_professores(self):
        return self.cnx.execute_query_read(self.q.read_all_teacher())
            
    
    def visualizar_professor(self, matricula: str):        
        return self.cnx.execute_query_read(self.q.read_teacher(), (matricula,))


    def atualizar_professor(self, id=None, p_nome=None, s_nome=None, matricula=None, data_nascimento=None, email=None):
        if id!=None and p_nome!=None and s_nome!=None and matricula!=None and data_nascimento!=None and email!=None:
            self.cnx.execute_query_update(self.q.update_teacher(),  p_nome,
                                                                    s_nome,
                                                                    matricula,
                                                                    data_nascimento,
                                                                    email,
                                                                    id)
            return "Dados atualizados com sucesso."
            
        elif id==None and p_nome!=None and s_nome==None and matricula==None and data_nascimento==None and email==None:
            self.cnx.execute_query_update(self.q.update_teacher_firstname, (p_nome,))
            return "Primeiro nome do professor atualizado com sucesso."

        elif id==None and p_nome==None and s_nome!=None and matricula==None and data_nascimento==None and email==None:
            self.cnx.execute_query_update(self.q.update_teacher_lastname(), (s_nome,))
            return "Sobrenome do professor atualizado com sucesso."
        
        elif id==None and p_nome==None and s_nome==None and matricula!=None and data_nascimento==None and email==None:
            self.cnx.execute_query_update(self.q.update_teacher_registration(), (matricula,))
            return "Matrícula do professor atualizada com sucesso."
        
        elif id==None and p_nome==None and s_nome==None and matricula==None and data_nascimento!=None and email==None:
            self.cnx.execute_query_update(self.q.update_teacher_birthday(), (data_nascimento,))
            return "Data de nascimento do professor atualizado com sucesso."

        elif id==None and p_nome==None and s_nome==None and matricula==None and data_nascimento==None and email!=None:
                self.cnx.execute_query_update(self.q.update_teacher_birthday(), (email,))
                return "E-mail do professor atualizado com sucesso."


    def ativar_inativar_professor(self, id=str, valor=bool):
        return self.cnx.execute_query_update(self.q.active_inactive(), (valor, id))


    def delete_professor(self, id: str):
        self.cnx.execute_query_update(self.q.delete_teacher(), (id,))


    def gerar_matricula(self):
        matriculas = self.cnx.execute_query_read(self.q.view_registration())
        ultima_matricula = int(matriculas[len(matriculas)-1][0][-1])

        if ultima_matricula<10:
            return "2025MP00" + str(ultima_matricula)
        elif ultima_matricula>10:
            return "2025MP0" + str(ultima_matricula)
        else:
            return "2025MP" + str(ultima_matricula)


    def encerrar_conexao(self):
        return self.cnx.close_connection()
        
    

class main():
    def __init__(self):
        self.e = Escola()
        
        while True:
            hm = self.home()

            if hm == "1":
                self.limpar_tela()
                matricula = self.e.gerar_matricula()
                p_nome = input("Primeiro nome: ")
                s_nome = input("Sobrenome: ")
                print("Data de nascimento")
                dia = int(input("\tDia: "))
                mes = int(input("\tMês: "))
                ano = int(input("\tAno: "))
                data_nasc = date(ano, mes, dia)
                email = input("E-mail: ")
                
                self.e.criar_professor(p_nome, s_nome, matricula, data_nasc, email)
                print(">>> Professor criado com sucesso.")
                sleep(1)

            elif hm == "2":
                self.limpar_tela()
                dados = self.e.visualizar_professores()
                for dado in dados:
                    print(f"""Nome: {dado[1]}
Sobrenome: {dado[2]}
Matricula: {dado[3]}
Data de Nascimento: {date.strftime(dado[4], "%d/%m/%Y")}
E-mail: {dado[5]}
Ativo: {'ATIVO' if int(dado[6]) else 'INATIVO'}
    """)
                input(">> Pressione enter para voltar.")

            elif hm == "3":
                self.limpar_tela()
                matricula = input("Digite a matrícula do professor: ")
                professor = self.e.visualizar_professor(matricula)

                for dado in professor:
                   print(f"""Nome: {dado[1]}
Sobrenome: {dado[2]}
Matricula: {dado[3]}
Data de Nascimento: {date.strftime(dado[4], "%d/%m/%Y")}
E-mail: {dado[5]}
Status: {'ATIVO' if int(dado[6]) else 'INATIVO'}
    """)   
                input(">> Pressione enter para voltar.")

            elif hm == "4":
                self.limpar_tela()
                id_professor = input("Digite o ID do professor: ")
                valor = input("Digite 1 para ativar e 0 para inativar o professor: ")
                self.e.ativar_inativar_professor(id_professor, valor)

                if valor == "0":
                    print(">>> Professor inativado com sucesso")
                    sleep(1)
                else:
                    print(">>> Professor ativado com sucesso")
                    sleep(1)

            elif hm == "5":
                self.limpar_tela()
                id_professor = input("Digite o id do professor que deseja excluir do banco\n>>> ")
                p_nome = Conexao().execute_query_read(Querie().view_firstname(), (id_professor,))
                excluir = input(f"Você está preste a excluir o professor {p_nome[0][0]}, você confirma?\n[ 1 ] - Sim\n[ 2 ] - Não\n>> ")
                if excluir == "1":
                    self.e.delete_professor(id_professor)
                    print(f"Professor de id {id_professor} excluido com sucesso")
                    sleep(1)
                else:
                    print(">> Operação abortada com sucesso.")
                    sleep(1)

            elif hm == "6":
                self.limpar_tela()
                self.e.encerrar_conexao()
                print("Programa encerrado.")
                break


    def home(self):
        while True:
            self.limpar_tela()
            user = input("""############ CRUD professor ############
[ 1 ] - Criar um novo professor
[ 2 ] - Visualizar TODOS os professores
[ 3 ] - Visualizar UM professor
[ 4 ] - Inativar/Ativar novo professor
[ 5 ] - Excluir um professor do banco
[ 6 ] - Encerrar
    -> """)
            if user in ["1","2","3","4","5", "6"]:
                break
        return user

    
    def limpar_tela(self):
        if os.name == "nt":
            return os.system("cls")
        else:
            return os.system("clear")

if __name__ == '__main__':
    main()
