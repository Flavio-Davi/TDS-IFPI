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
            

    def execute_query(self, query):
        self._cursor.execute(query)
        result = self._cursor.fetchall()
        self._cursor.close()
        self._cnx.close()
        
        return result
    
    
    def execute_long_query(self, query, value):
        self._cursor.execute(query, value)
        self._cnx.commit()
        self._cursor.close()
        self._cnx.close()
        
        return True


if __name__ == '__main__':
    Conexao()
