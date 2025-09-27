import mysql.connector
from mysql.connector import errorcode
from dotenv import load_dotenv
from os import getenv

class Db_config:
    def __init__(self):
        load_dotenv(r'.\database\config.env')
        self.__USER = getenv("USER")
        self.__PASSWORD = getenv("PASSWORD")
        self.__HOST = getenv("HOST")
        self.__DB_NAME = getenv("DB_NAME")
        self.__PORT = getenv("PORT")

    @property
    def user(self):
        return self.__USER
    @property
    def password(self):
        return self.__PASSWORD
    @property
    def host(self):
        return self.__HOST
    @property
    def db_name(self):
        return self.__DB_NAME
    @property
    def port(self):
        return self.__PORT


class Conexao(Db_config):
    def __init__(self):
        super().__init__()
        try:
            self._config = {
                'user': self.user, 'password': self.password,
                'host': self.host,
                'database': self.db_name
            }
            self._cnx = mysql.connector.connect(**self._config)
            self._cursor = self._cnx.cursor()

        except mysql.connector.Error as e:
            if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                raise "ERROR: Acesso ao banco negado. Verifique suas credenciais."
            elif e.errno == errorcode.ER_BAD_DB_ERROR:
                raise f"ERROR: Banco de dados *{self.db_name}* inexistente."
            else:
                raise Exception(e)


    def execute_query_read(self, query: str, param: tuple | None=None):
        try:
            self._cursor.execute(query, param)
            result = self._cursor.fetchall()
        except Exception as e:
            raise Exception(e)
        return result


    def execute_query_update(self, query: str, param: tuple):
        try:
            self._cursor.execute(query, param)
            self._cnx.commit()
        except Exception as e:
            raise Exception(e)
        return True


    def close_connection(self):
        self._cursor.close()
        self._cnx.close()

        return "Conexão encerrada"
