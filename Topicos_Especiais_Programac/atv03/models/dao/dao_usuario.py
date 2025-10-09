from database.config.conexao import Conexao
from database.queries.usuarios.queries_usuario import Queries_usuario
from models.model.model_usuario import Usuario


class Dao_Usuario:
    def __init__(self):
        self.__cnx = Conexao()


    def create(self, usuario: Usuario):
        try:
            new_user = self.__cnx.execute_query_update(Queries_usuario.create(), (usuario.nome,
                                                                    usuario.email,
                                                                    usuario.data_nascimento))
            data_new_user = self.__cnx.execute_query_read(Queries_usuario.read(True), (new_user,))
            data = Usuario(id=data_new_user[0][0],
                           nome=data_new_user[0][1],
                           email=data_new_user[0][2],
                           data_nascimento=data_new_user[0][3])
            
        except Exception as e:
            raise Exception(e)

        return data


    def read(self, id: int | None=None):
        try:
            if id:
                data = self.__cnx.execute_query_read(Queries_usuario.read(True), (id,))
                user = Usuario(id=data[0][0],
                               nome=data[0][1],
                               email=data[0][2],
                               data_nascimento=data[0][3])
            else:
                data = self.__cnx.execute_query_read(Queries_usuario.read())
        except Exception as e:
            raise Exception(e)
        
        return user
    

    def update(self, user: Usuario):
        try:
            self.__cnx.execute_query_update(Queries_usuario.update(), (user.id,
                                                  user.nome,
                                                  user.email,
                                                  user.data_nascimento,
                                                  user.id))
            new_data = self.__cnx.execute_query_read(Queries_usuario.read(True), (user.id,))
            return new_data

        except Exception as e:
            raise Exception(e)


    def delete(self):
        pass
