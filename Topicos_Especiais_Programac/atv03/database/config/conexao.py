from dotenv import load_dotenv
from os import getenv, path
from mysql.connector import connect
from mysql.connector import Error


class metadata:
    def __init__(self):
        __dir_metaData = path.abspath(r'database\config\.env')
        load_dotenv(__dir_metaData)
        self._USER = getenv("USER")
        self._PASSWORD = getenv("PASSWORD")
        self._HOST = getenv("HOST")
        self._DATABASE = getenv("DATABASE")
        print(self._USER)


class Conexao(metadata):
    def __init__(self):
        super().__init__()
        try:
            self.__cnx = connect(user = self._USER, password=self._PASSWORD,
                        host=self._HOST,
                        database=self._DATABASE)
            self.__cursor = self.__cnx.cursor()
        except Error as e:
            raise(e)


    def execute_query_read(self, query: str, param: tuple | None=None):
        try:
            self.__cursor.execute(query, param)
            self.data = self.__cursor.fetchall()
            return self.data
        except Exception as e:
            raise(e)
        

    def execute_query_update(self, query: str, param: tuple):
        try:
            self.__cursor.execute(query, param)
            self.__cnx.commit()

            new_id = self.__cursor.lastrowid
            return new_id if new_id !=0 else True
        except Exception as e:
            raise(e)


    def close_connection(self):
        try:
            self.__cursor.close()
            self.__cnx.close()
            return True
        except Exception as e:
            raise(e)
