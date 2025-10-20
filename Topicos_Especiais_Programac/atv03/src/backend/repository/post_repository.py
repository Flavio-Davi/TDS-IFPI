from src.backend.infra.database import Database
from src.backend.model.post_model import Post

class PostRepository:
    @staticmethod
    def create(post: Post):
        query = """
                INSERT INTO 
                    posts (id_user, data_hora, conteudo, midia) 
                VALUES (%s, %s, %s, %s);
                """
        params = (post.id_user, post.data_hora, post.conteudo, post.midia)
        return Database.execute_query(query, params, commit=True)

    @staticmethod
    def get_by_id(post_id: int):
        query = """
                SELECT 
                    id, 
                    id_user, 
                    data_hora, 
                    conteudo, 
                    midia 
                FROM 
                    posts 
                WHERE 
                    id = %s"""
        result = Database.execute_query(query, (post_id,), fetch_one=True)
        if result:
            return Post(**result)
        return None

    @staticmethod
    def get_by_user_id(user_id: int):
        query = """
                SELECT 
                    id, 
                    id_user, 
                    data_hora, 
                    conteudo, 
                    midia 
                FROM 
                    posts 
                WHERE 
                    id_user = %s 
                ORDER BY 
                    data_hora DESC;
                """
        results = Database.execute_query(query, (user_id,), fetch_all=True)
        return [Post(**result) for result in results] if results else []

    @staticmethod
    def get_all():
        query = """
                SELECT 
                    id, 
                    id_user, 
                    data_hora, 
                    conteudo, 
                    midia 
                FROM 
                    posts 
                ORDER BY 
                    data_hora DESC"""
        results = Database.execute_query(query, fetch_all=True)
        return [Post(**result) for result in results] if results else []

    @staticmethod
    def update(post: Post):
        query = """
                UPDATE 
                    posts 
                SET 
                    id_user = %s, 
                    data_hora = %s, 
                    conteudo = %s, 
                    midia = %s 
                WHERE 
                    id = %s;
                """
        params = (post.id_user, post.data_hora, post.conteudo, post.midia, post.id)
        return Database.execute_query(query, params, commit=True)

    @staticmethod
    def delete(post_id: int):
        query = """
                DELETE FROM 
                    posts 
                WHERE 
                    id = %s;
                """
        return Database.execute_query(query, (post_id,), commit=True)

