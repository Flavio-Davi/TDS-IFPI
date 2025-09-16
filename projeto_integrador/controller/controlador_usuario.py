from models.usuario import DAO_Usuario
from models.usuario import Usuario
import string
import random

class controle_usuario:
    def __init__(self):
        self.__DAO = DAO_Usuario()
    
    def __token(self):
        __letras_mai = string.ascii_uppercase
        __letras_min = string.ascii_lowercase
        __simbolos = string.digits

        data_token = __letras_min+__letras_mai+__simbolos
        __token = ""
        for c in range(10):
            __token+=random.sample(data_token, 1)[0]

        return __token 

    @__token
    def token(self):
        return self.__token()

    def create_usuario(self, usuario: Usuario):
        self.__DAO.create(
            usuario
        )

        return 201
   
    def readme_usuario(self):
        dados = self.__DAO.read()           

        return dados

    def update_usuario(self, usuario: Usuario):
        self.__DAO.update(usuario.id, usuario.nome, usuario.email, usuario.contato)

        return 201
   
    def delete_usuario(self, usuario: Usuario):
        self.__DAO.delete(usuario.id)

        return 201

