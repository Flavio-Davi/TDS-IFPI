import mysql.connector
from dotenv import load_dotenv
from os import getenv

class Db_config:
    def __init__(self):
        load_dotenv('./config.env')
        self.__user = getenv('USER')
        self.__password = getenv('PASSWORD')
        self.__host = getenv('HOST')
        self.__database = getenv('DATABASE')

    @property
    def user(self):
        return self.__user
    @property
    def password(self):
        return self.__password
    @property
    def host(self):
        return self.__host
    @property
    def database(self):
        return self.__database



class Conexao(Db_config):
    def __init__(self):
        super().__init__()
        try:
            self._config = {
                'user': self.user, 'password': self.password,
                'host': self.host,
                'database': self.database
            }
            self._cnx = mysql.connector.connect(**self._config)
            self._cursor = self._cnx.cursor()

        except mysql.connector.Error as e:
                raise Exception(e)


    def execute_query_read(self, query: str, param: tuple |None=None):
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


if __name__ == '__main__':
    Conexao()
    
