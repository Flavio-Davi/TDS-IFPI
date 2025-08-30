import mysql.connector
from mysql.connector import errorcode
from dotenv import load_dotenv
from os import getenv

load_dotenv(r'.\config.env')

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
                print("ERROR: Acesso ao banco negado. Verifique suas credenciais.")
            elif e.errno == errorcode.ER_BAD_DB_ERROR:
                print(f"ERROR: Banco de dados *{DB_NAME}* inexistente.")
            else:
                print(f"ERROR: {e}")
            

    def execute_query_read(self, query, param=None):
        try:
            self._cursor.execute(query, param)
            result = self._cursor.fetchall()
            self._cursor.close()
            self._cnx.close()
        except mysql.connector.Error as e:
            print(f"ERROR: {e}")
        return result
    
        
    def execute_query_update(self, query, param):
        try:
            self._cursor.execute(query, param)
            self._cnx.commit()
            self._cursor.close()
            self._cnx.close()
        except mysql.connector.Error as e:
            return f"ERROR: {e}"
        return True


if __name__ == '__main__':
    Conexao()
