from fastapi.encoders import jsonable_encoder
from database.conexao import Conexao
from pydantic import BaseModel, Field
from datetime import date
from ulid import ULID


class Aluno(BaseModel):
    matricula: str = Field(default_factory=lambda: str(ULID()))
    nome_completo: str
    data_nascimento: date
    cpf: str


class DAO_Aluno:
    def __init__(self):
        self.__cnx = Conexao()


    def create(self, aluno: Aluno):
        QUERY = """INSERT INTO 
                        aluno (matricula, nome_completo, data_nascimento, cpf)
                    VALUES
                        (%s, %s, %s, %s)"""
        try:
            self.__cnx.execute_query_update(QUERY, (aluno.matricula, 
                                                    aluno.nome_completo, 
                                                    aluno.data_nascimento, 
                                                    aluno.cpf))
        except Exception as e:
            raise(e)
        
        return 201

    def read(self, aluno: Aluno | None=None):
        try:
            dados: list[Aluno] = []
            if aluno:
                QUERY = f"""SELECT * FROM aluno WHERE matricula=%s"""
                dado = self.__cnx.execute_query_read(QUERY, (aluno.matricula,))
            else:
                QUERY = """SELECT * FROM aluno"""
                dado = self.__cnx.execute_query_read(QUERY)
            for a in dado:
                dados.append(Aluno(matricula=a[0],
                                   nome_completo=a[1],
                                   data_nascimento=a[2],
                                   cpf=a[3]))
            return jsonable_encoder(dados)
        except Exception as e:
            raise(e)

    def update(self, aluno: Aluno, new_name: str | None, new_date: date | None):
        try:
            col_bd=['nome_completo', 'data_nascimento']
            var_func = [new_name, new_date]
            update_col = []
            var_get = []

            for col, var in zip(col_bd, var_func):
                if var is not None:
                    update_col.append(f'{col}=%s')
                    var_get.append(var)
            
            if update_col:
                clause = ", ".join(update_col)
                QUERY = f"""
                        UPDATE
                            aluno
                        SET
                            {clause}
                        WHERE
                            matricula=%s"""
                var_get.append(aluno.matricula)
                self.__cnx.execute_query_update(QUERY, var_get)
            return 201
        except Exception as e:
            raise(e)
        
    def delete(self, aluno: Aluno):
        try:
            QUERY = """DELETE FROM aluno WHERE matricula=%s;"""
            self.__cnx.execute_query_update(QUERY, (aluno.matricula))
            return 201
        except Exception as e:
            raise(e)
