from settings_db.db_config import Conexao
from models.model.aluno import Aluno

class Endereco:
    def __init__(self, cidade: str, rua: str | None = None,  numero: str | None = None, bairro: str | None = None, cep: str | None = None):
        self.__rua = rua
        self.__numero = numero
        self.__bairro = bairro
        self.__cidade = cidade
        self.__cep = cep
        self.id: int


class DAO_Endereco:
    def __init__(self):
        self.__cnx = Conexao()

    
    def create(self, endereco: Endereco, aluno: Aluno):
        QUERY = """
                INSERT INTO
                    endereco(cidade, aluno)
                VALUES

"""

        self.__cnx.execute_query_update(QUERY, (endereco.__cidade, aluno.matricula))
