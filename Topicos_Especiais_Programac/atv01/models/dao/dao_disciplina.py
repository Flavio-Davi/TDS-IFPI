from database.conexao import Conexao
from models.model.disciplina import Disciplina
from models.queries.querie_disciplina import Querie_disciplina


class DAO_Disciplina:
    def __init__(self):
        self.__cnx = Conexao()
        self.__querie = Querie_disciplina()

    def create(self, disciplina: Disciplina) -> str:
        dado = (disciplina.codigo, 
                disciplina.nome, 
                disciplina.descricao, 
                disciplina.id_professor, 
                disciplina.carga_horaria)
        self.__cnx.execute_query_update(self.__querie.create(), dado)

        return 201

    def read(self, id:int | None=None) -> str:
        dado: list[Disciplina]=[]
        if id:
            dados = self.__cnx.execute_query_read(self.__querie.read(True), (id,))
        else:
            dados = self.__cnx.execute_query_read(self.__querie.read())
        for c in dados:
            dado.append(Disciplina(
                id=c[0],
                codigo=c[1],
                nome=c[2],
                descricao=c[3],
                id_professor=c[4],
                carga_horaria=c[5],
            ))

        return dado

    def update(self, codigo: str, nome=None, descricao=None, id_professor=None, carga_horaria=None) -> str:
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

        valores.append(codigo)
        self.__cnx.execute_query_update(self.__querie.update(campos), valores)
        
        return 201

    def delete(self, id:int) -> str:
        self.__cnx.execute_query_update(self.__querie.delete(), (id,))
        return True