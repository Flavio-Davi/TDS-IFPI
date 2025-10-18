from src.infra.mysql_connector.config.database import Conexao
from src.infra.mysql_connector.queries.user_query import User_query
from src.schema.user import BaseUser, CreateUser, UpdateUser


class User_service:
    def __init__(self):
        self.__cnx = Conexao()
        self.__query = User_query() 
    
    def create_user(self, user: CreateUser) -> int:
        create = self.__cnx.execute_query_update(self.__query.create(), user.nome,
                                                                        user.email,
                                                                        user.data_nascimento)
        return create
    
    def read_user(self, user: UpdateUser | None=None) -> BaseUser:
        if user:
            data = self.__cnx.execute_query_read(self.__query.read(id=True), user.id)
        else:
            data = self.__cnx.execute_query_read(self.__query.read())

        data_return =  BaseUser(nome=data[0],
                                email=data[1],
                                data_nascimento=data[2])
        return data_return
    
    def update_user(self, user: UpdateUser):
        self.__cnx.execute_query_update(self.__query.update(**user), **user.values())

    