import mysql.connector
from dotenv import load_dotenv
import os

class db_config:
    def __init__(self):
        load_dotenv(r'.\database\db_config.env')
        self._user = os.getenv("USER")
        self._password = os.getenv("PASSWORD")
        self._host = os.getenv("HOST")
        self._db_name = os.getenv("DB_NAME")


class Conexao:
    def __init__(self):
        self.__db = db_config()
        try:
            self.__cnx = mysql.connector.connect(user=self.__db._user, password=self.__db._password,
                                        host=self.__db._host, database=self.__db._db_name)
            print(">> Conectado.")
            self.__cursor = self.__cnx.cursor()
        except Exception as e:
            raise(e)
    
    def inserir_alterar_dados(self, query: str, param: tuple | None=None):
        try:
            self.__cursor.execute(query, param)
            self.__cnx.commit()
            return ">>> Ação realizada com sucesso."
        except Exception as e:
            raise(e)

    def visualizar_dados(self, query: str, param: tuple | None=None):
        try:
            if param:
                self.__cursor.execute(query, param)
            else:
                self.__cursor.execute(query, ())
            dados = self.__cursor.fetchall()
            return dados
        except Exception as e:
            raise(e)

    def encerrar_conexao(self):
        self.__cnx.close()
        return ">>> Conexão encerrada."


if __name__ == '__main__':
    Conexao()
