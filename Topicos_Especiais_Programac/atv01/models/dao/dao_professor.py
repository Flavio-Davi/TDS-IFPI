from database.conexao import Conexao
from models.model.professor import Professor
from models.queries.querie_professor import Querie_professor
from datetime import date


class DAO_Professor: 
    def __init__(self):
        self.__cnx = Conexao()
        self.__querie = Querie_professor()

    def create_teacher(self, professor: Professor) -> str:
        param = (professor.nome_completo, professor.matricula, professor.data_nascimento, professor.email, professor.status)
        self.__cnx.execute_query_update(self.__querie.create(), param)
        return ">> Professor criado com sucesso."

    def read(self, matricula: str | None=None) -> str:
        dado: list[Professor]=[]
        if matricula:
            dados = self.__cnx.execute_query_read(self.__querie.read(True), (matricula,))
        else:
            dados = self.__cnx.execute_query_read(self.__querie.read())

        for c in dados:
            dado.append(Professor(
                id=c[0],
                nome_completo=c[1],
                matricula=c[2],
                data_nascimento=c[3],
                email=c[4],
                status=c[5],
            ))
        return dado

    def update(self, professor: Professor, new_name:str | None=None, new_matrica:str | None=None, new_data:date | None=None, new_email:str | None=None, new_status:str | None=None) -> str:
        try:
            col_bd=['nome_completo', 'matricula', 'data_nascimento', 'email', 'status']
            var_func = [new_name, new_matrica, new_data, new_email, new_status]
            update_col = []
            var_get = []

            for col, var in zip(col_bd, var_func):
                if var is not None:
                    update_col.append(f'{col}=%s')
                    var_get.append(var)
            
            if update_col:
                clause = ", ".join(update_col)
                var_get.append(professor.matricula)
                self.__cnx.execute_query_update(self.__querie.update(clause), (var_get,))
            return 201
        except Exception as e:
            raise(e)

    def delete(self, id: int):
        self.__cnx.execute_query_update(self.__querie.delete(), (id,))
        return True
