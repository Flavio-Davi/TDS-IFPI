from pydantic import BaseModel
from database.conexao import Conexao
from ulid import ULID

class Cidade(BaseModel):
    id: str | None = str(ULID())
    nome: str
    estado: str
    pib: int | None = None
    populacao: int 


class DAO_Cidade:
    def __init__(self):
        self.__cnn = Conexao()
    
    def create_city(self, cidade: Cidade):
        try:
            QUERY = """
                INSERT INTO 
                    cidade(id_user, nome, estado, pib, populacao)
                VALUES
                    (%s, %s, %s, %s, %s);"""
            self.__cnn.update(QUERY, (cidade.id, cidade.nome, cidade.estado, cidade.pib, cidade.populacao))        
        except Exception as e:
            raise(e)
        self.__cnn.close_connection()
        return {"ID": cidade.id,
                "NOME": cidade.nome,
                "ESTADO": cidade.estado,
                "PIB": cidade.pib,
                "POPULAÇÃO": cidade.populacao}
