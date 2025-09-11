from database.conexao import Conexao

class Usuario:
    def __init__(self, nome: str, email: str, num_cel: int):
        self.nome = nome
        self.email = email
        self.num_cel = num_cel


class DAO_Usuario:
    def __init__(self):
        self.__cnx = Conexao()

    def create(self, usuario: Usuario):
        QUERY = """INSERT INTO usuario (nome_completo, email, numero_cel) VALUES (%s, %s, %s);"""
        self.__cnx.inserir_alterar_dados(QUERY, (usuario.nome, usuario.email, usuario.num_cel))

        return ">>> Dados inseridos com sucesso."

    def read(self, id: int | None=None):
        if id:
            QUERY = """SELECT nome_completo, email, numero_cel FROM usuario WHERE id=%s"""
            dados = self.__cnx.visualizar_dados(QUERY, id)
            return dados
        else:
            QUERY = """SELECT nome_completo, email, numero_cel FROM usuario"""
            dados = self.__cnx.visualizar_dados(QUERY)
            return dados

    def update(self, id: int, nome: str | None=None, email: str | None=None, num_cel: str | None=None):
        if nome:
            QUERY = """UPDATE nome SET nome_completo=%s WHERE id=%s"""
            self.__cnx.inserir_alterar_dados(QUERY, (nome, id))
        elif email:
            QUERY = """UPDATE usuario SET email=%s WHERE id=%s"""
            self.__cnx.inserir_alterar_dados(QUERY, (email, id))
        elif num_cel:
            QUERY = """UPDATE usuario SET numero_cel=%s WHERE id=%s"""
            self.__cnx.inserir_alterar_dados(QUERY, (num_cel, id))
        elif nome and email:
            QUERY = """UPDATE usuario, email SET nome_completo=%s, email=%s WHERE id=%s"""
            self.__cnx.inserir_alterar_dados(QUERY, (nome, email, id))
        elif nome and num_cel:
            QUERY = """UPDATE usuario SET nome_completo=%s, numero_cel=%s WHERE id=%s"""
            self.__cnx.inserir_alterar_dados(QUERY, (nome, num_cel, id))
        elif email and num_cel:
            QUERY = """UPDATE usuario SET email=%s, numero_cel=%s WHERE id=%s"""
            self.__cnx.inserir_alterar_dados(QUERY, (email, num_cel, id))
        else:
            QUERY = """UPDATE usuario SET nome_completo=%s, email=%s, numero_cel=%s WHERE id=%s"""
            self.__cnx.inserir_alterar_dados(QUERY, (nome, email, num_cel, id))

            return "Alteração realizada com sucesso"

    def delete(self, id: int):
        QUERY_NOME = """SELECT nome_completo FROM usuario WHERE id = %s"""
        nome = self.__cnx.visualizar_dados(QUERY_NOME, (id,))
        QUERY = """DELETE FROM usuario WHERE id = %s;"""
        self.__cnx.inserir_alterar_dados(QUERY, (id,))

        return f">>> Usuario {nome[0][0]} deletado com sucesso."
