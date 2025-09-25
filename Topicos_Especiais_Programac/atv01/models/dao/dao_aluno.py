from settings_db.db_config import Conexao
from models.model.endereco import Endereco
from models.model.aluno import Aluno


class DAO_Aluno:
    def __init__(self):
        self.__cnx = Conexao()

    
    def create(self, aluno: Aluno, endereco: Endereco):
        QUERY = """
                INSERT INTO
                    aluno(matricula, cpf, nome_completo, data_nascimento, id_endereco)
                VALUES
                    (%s, %s, %s, %s, %s, %s)
"""
        self.__cnx.execute_query_update(aluno.matricula,
                                        aluno.cpf,
                                        aluno.nome_completo,
                                        aluno.data_nascimento)
