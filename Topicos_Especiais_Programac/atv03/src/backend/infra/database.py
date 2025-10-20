import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path='.env')

class Database:
    _connection = None

    @classmethod
    def get_connection(cls):
        if cls._connection is None:
            try:
                cls._connection = mysql.connector.connect(
                    host=os.getenv('DB_HOST'),
                    user=os.getenv('DB_USER'),
                    password=os.getenv('DB_PASSWORD'),
                    database=os.getenv('DB_NAME')
                )
                print(">>> Conexão com o banco de dados estabelecida com sucesso!")
            except mysql.connector.Error as e:
                print(f">>> Erro ao conectar no banco de dados: {e}")
                cls._connection = None
        return cls._connection

    @classmethod
    def close_connection(cls):
        if cls._connection and cls._connection.is_connected():
            cls._connection.close()
            cls._connection = None
            print(">>> Conexão com o banco encerrada.")

    @classmethod
    def execute_query(cls, query, params=None, fetch_one=False, fetch_all=False, commit=False):
        connection = cls.get_connection()
        if connection is None:
            return None

        cursor = connection.cursor(dictionary=True)
        try:
            cursor.execute(query, params)
            if commit:
                connection.commit()
                return cursor.rowcount
            if fetch_one:
                return cursor.fetchone()
            if fetch_all:
                return cursor.fetchall()
            return None
        except mysql.connector.Error as e:
            print(f">>> Erro ao executar query: {e}")
            connection.rollback()
            return None
        finally:
            cursor.close()

