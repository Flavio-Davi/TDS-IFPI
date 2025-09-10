import mysql.connector
from mysql.connector import errorcode
from dotenv import load_dotenv
from os import getenv

load_dotenv(r'.\settings_db\config.env')

USER = getenv("USER")
PASSWORD = getenv("PASSWORD")
HOST = getenv("HOST")
DB_NAME = getenv("DB_NAME")
PORT = getenv("PORT")

class Conexao:
    def __init__(self):
        try:
            self._config = {
                'user': USER, 'password': PASSWORD,
                'host': HOST,
                'database': DB_NAME,
                'raise_on_warnings': True
            }
            self._cnx = mysql.connector.connect(**self._config)
            self._cursor = self._cnx.cursor()

        except mysql.connector.Error as e:
            if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                raise "ERROR: Acesso ao banco negado. Verifique suas credenciais."
            elif e.errno == errorcode.ER_BAD_DB_ERROR:
                raise f"ERROR: Banco de dados *{DB_NAME}* inexistente."
            else:
                raise Exception(e)


    def execute_query_read(self, query, param=None):
        try:
            self._cursor.execute(query, param)
            result = self._cursor.fetchall()
        except Exception as e:
            raise Exception(e)
        return result


    def execute_query_update(self, query, param):
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
