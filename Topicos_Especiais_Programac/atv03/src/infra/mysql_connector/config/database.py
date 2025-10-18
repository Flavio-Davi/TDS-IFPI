from dotenv import find_dotenv
from dotenv import load_dotenv
from os import getenv
from mysql.connector import connect
from mysql.connector import Error


class metadata:
    def __init__(self):
        load_dotenv(find_dotenv('.env'))
        self._USER = getenv("USER")
        self._PASSWORD = getenv("PASSWORD")
        self._HOST = getenv("HOST")
        self._DATABASE = getenv("DATABASE")


class Conexao(metadata):
    def __init__(self):
        super().__init__()
        try:
            self.__cnx = connect(user=self._USER, password=self._PASSWORD,
                                 host=self._HOST,
                                 database=self._DATABASE)
            self.__cursor = self.__cnx.cursor()

        except Error as e:
            raise e


    def execute_query_read(self, query: str, *param):
        try:
            self.__cursor.execute(query, param)
            self.data = self.__cursor.fetchall()
            return self.data
        
        except Exception as e:
            raise e

    def execute_query_update(self, query: str, *param):
        try:
            self.__cursor.execute(query, param)
            self.__cnx.commit()            
            new_id = self.__cursor.lastrowid

            return new_id if new_id !=0 else True
        
        except Exception as e:
            self.__cnx.rollback()
            raise e

    def close_connection(self):
        try:
            self.__cursor.close()
            self.__cnx.close()
        except Exception as e:
            raise e
        
