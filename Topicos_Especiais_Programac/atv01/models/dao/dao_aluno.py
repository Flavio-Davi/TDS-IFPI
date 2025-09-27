from fastapi.encoders import jsonable_encoder
from database.conexao import Conexao
from models.model.aluno import Aluno
from models.queries.querie_aluno import Querie_aluno
from datetime import date


class DAO_Aluno:
    def __init__(self):
        self.__cnx = Conexao()
        self.__querie = Querie_aluno()


    def create(self, aluno: Aluno) -> str:
        try:
            self.__cnx.execute_query_update(self.__querie.create(), (aluno.matricula, 
                                                    aluno.nome_completo, 
                                                    aluno.data_nascimento, 
                                                    aluno.cpf))
        except Exception as e:
            raise(e)
        
        return 201

    def read(self, aluno: Aluno | None=None) -> str:
        try:
            dados: list[Aluno] = []
            if aluno:
                dado = self.__cnx.execute_query_read(self.__querie.read(True), (aluno.matricula,))
            else:
                dado = self.__cnx.execute_query_read(self.__querie.read())
            for a in dado:
                dados.append(Aluno(matricula=a[0],
                                   nome_completo=a[1],
                                   data_nascimento=a[2],
                                   cpf=a[3]))
            return dados
        except Exception as e:
            raise(e)

    def update(self, aluno: Aluno, new_name: str | None, new_date: date | None, new_cpf: str | None=None) -> str:
        try:
            col_bd=['nome_completo', 'data_nascimento', 'cpf']
            var_func = [new_name, new_date, new_cpf]
            update_col = []
            var_get = []

            for col, var in zip(col_bd, var_func):
                if var is not None:
                    update_col.append(f'{col}=%s')
                    var_get.append(var)
            
            if update_col:
                clause = ", ".join(update_col)
                var_get.append(aluno.matricula)
                self.__cnx.execute_query_update(self.__querie.update(clause), (var_get,))
            return 201
        except Exception as e:
            raise(e)
        
    def delete(self, id_aluno) -> str:
        try:
            self.__cnx.execute_query_update(self.__querie.delete(), (id_aluno,))
            return True
        except Exception as e:
            raise(e)
