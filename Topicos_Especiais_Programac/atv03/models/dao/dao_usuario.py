from database.config.conexao import Conexao
from database.queries.usuarios.queries_usuario import Queries_usuario
from models.model.model_usuario import Usuario


class Dao_Usuario:
    def __init__(self):
        self.__cnx = Conexao()
        self.__querie = Queries_usuario()


    def create(self, usuario: Usuario):
        try:
            new_user = self.__cnx.execute_query_update(self.__querie.create(), (usuario.nome,
                                                                    usuario.email,
                                                                    usuario.data_nascimento))
            return self.__cnx.execute_query_read(self.__querie.read(True), (new_user,))
        except Exception as e:
            raise(e)                


    def read(self, id: int | None=None):
        if id:
            data = self.__cnx.execute_query_read(self.__querie.read(True), id)
        else:
            data = self.__cnx.execute_query_read(self.__querie.read())
        return data


    def update(self):
        pass
    def delete(self):
        pass
