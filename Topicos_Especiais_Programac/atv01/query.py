from datetime import date
from db_config import Conexao

class Querie:
    def __init__(self):
        self.cnx = Conexao()


    def all_data(self):
        QUERY = "SELECT * FROM professor;"
        return QUERY
    

    def insert_data(self):
        QUERY = """INSERT INTO professor
    (primeiro_nome, sobrenome, matricula, data_nascimento, email)
VALUES
    (%s, %s, %s, %s, %s);"""

        return QUERY
    

if __name__ == '__main__':
    Querie()