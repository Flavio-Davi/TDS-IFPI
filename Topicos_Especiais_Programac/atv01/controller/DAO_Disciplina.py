from settings_db.db_config import Conexao
from models.modelo_disciplina import Disciplina

class DAO_Disciplina:
    def __init__(self):
        self.__cnx = Conexao()

    @property
    def cnx(self):
        return self.__cnx

    def create(self, disciplina: Disciplina):
        QUERY = f'''INSERT INTO disciplina (codigo, nome, descricao, id_professor, carga_horaria)
                    VALUES (
                        %s, %s, %s,
                        (SELECT pr.id FROM professor pr WHERE pr.matricula = %s),
                        %s
                    );'''
        dado = (disciplina.codigo, disciplina.nome, disciplina.descricao, disciplina.professor.matricula, disciplina.carga_horaria)
        self.cnx.execute_query_update(QUERY, dado)

    def read(self):
        QUERY = '''SELECT * FROM disciplina;'''
        dados = self.cnx.execute_query_read(QUERY)
        return dados

    def update(self, codigo: str, nome=None, descricao=None, id_professor=None, carga_horaria=None):
        campos = []
        valores = []

        if nome is not None:
            campos.append("nome = %s")
            valores.append(nome)
        if descricao is not None:
            campos.append("descricao = %s")
            valores.append(descricao)
        if id_professor is not None:
            campos.append("id_professor = %s")
            valores.append(id_professor)
        if carga_horaria is not None:
            campos.append("carga_horaria = %s")
            valores.append(carga_horaria)

        if not campos:
            return

        QUERY = f"UPDATE disciplina SET {', '.join(campos)} WHERE codigo = %s"
        valores.append(codigo)
        self.cnx.execute_query_update(QUERY, valores)
        
        return 201

    def delete(self):
        pass
