from src.backend.infra.database import Database
from src.backend.model.usuario_model import Usuario

class UsuarioRepository:
    @staticmethod
    def create(usuario: Usuario):
        query = """
                INSERT INTO 
                    usuarios (nome_completo, email, data_nascimento) 
                VALUES (%s, %s, %s);
                """
        params = (usuario.nome_completo, usuario.email, usuario.data_nascimento)
        return Database.execute_query(query, params, commit=True)

    @staticmethod
    def get_by_id(user_id: int):
        query = """
                SELECT 
                    id, 
                    nome_completo, 
                    email, 
                    data_nascimento 
                FROM 
                    usuarios 
                WHERE 
                    id = %s;
                """
        result = Database.execute_query(query, (user_id,), fetch_one=True)
        if result:
            return Usuario(**result)
        return None

    @staticmethod
    def get_all():
        query = """
                SELECT 
                    id, 
                    nome_completo, 
                    email, 
                    data_nascimento 
                FROM 
                    usuarios;
                """
        results = Database.execute_query(query, fetch_all=True)
        return [Usuario(**result) for result in results] if results else []

    @staticmethod
    def update(usuario: Usuario):
        query = """
                UPDATE 
                    usuarios 
                SET 
                    nome_completo = %s, 
                    email = %s, 
                    data_nascimento = %s 
                WHERE 
                    id = %s;
                """
        params = (usuario.nome_completo, usuario.email, usuario.data_nascimento, usuario.id)
        return Database.execute_query(query, params, commit=True)

    @staticmethod
    def delete(user_id: int):
        query = """
                DELETE FROM 
                    usuarios 
                WHERE 
                    id = %s;
                """
        return Database.execute_query(query, (user_id,), commit=True)

