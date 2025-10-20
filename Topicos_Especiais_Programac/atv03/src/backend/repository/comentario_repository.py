from src.backend.infra.database import Database
from src.backend.model.comentario_model import Comentario

class ComentarioRepository:
    @staticmethod
    def create(comentario: Comentario):
        query = """
                INSERT INTO 
                    comentarios (id_user, id_post, conteudo, data_hora) 
                VALUES (%s, %s, %s, %s);
                """
        params = (comentario.id_user, comentario.id_post, comentario.conteudo, comentario.data_hora)
        return Database.execute_query(query, params, commit=True)

    @staticmethod
    def get_by_id(comentario_id: int):
        query = """
                SELECT 
                    id, 
                    id_user, 
                    id_post, 
                    conteudo, 
                    data_hora 
                FROM 
                    comentarios 
                WHERE 
                    id = %s;
                """
        result = Database.execute_query(query, (comentario_id,), fetch_one=True)
        if result:
            return Comentario(**result)
        return None

    @staticmethod
    def get_by_post_id(post_id: int):
        query = """
                SELECT 
                    id, 
                    id_user, 
                    id_post, 
                    conteudo, 
                    data_hora 
                FROM 
                    comentarios 
                WHERE 
                    id_post = %s 
                ORDER BY 
                    data_hora DESC;
                """
        results = Database.execute_query(query, (post_id,), fetch_all=True)
        return [Comentario(**result) for result in results] if results else []

    @staticmethod
    def get_by_user_id(user_id: int):
        query = """
                SELECT
                    id,
                    id_user,
                    id_post,
                    conteudo,
                    data_hora
                FROM
                    comentarios
                WHERE
                    id_user = %s 
                ORDER BY
                    data_hora DESC;
                """
        results = Database.execute_query(query, (user_id,), fetch_all=True)
        return [Comentario(**result) for result in results] if results else []

    @staticmethod
    def get_all():
        query = """
                SELECT 
                    id, 
                    id_user, 
                    id_post, 
                    conteudo, 
                    data_hora 
                FROM 
                    comentarios 
                ORDER BY 
                    data_hora DESC;
                """
        results = Database.execute_query(query, fetch_all=True)
        return [Comentario(**result) for result in results] if results else []

    @staticmethod
    def update(comentario: Comentario):
        query = """
                UPDATE 
                    comentarios 
                SET 
                    id_user = %s, 
                    id_post = %s, 
                    conteudo = %s, 
                    data_hora = %s 
                WHERE 
                    id = %s;
                """
        params = (comentario.id_user, comentario.id_post, comentario.conteudo, comentario.data_hora, comentario.id)
        return Database.execute_query(query, params, commit=True)

    @staticmethod
    def delete(comentario_id: int):
        query = """
                DELETE FROM 
                    comentarios 
                WHERE 
                    id = %s;"""
        return Database.execute_query(query, (comentario_id,), commit=True)

