from src.backend.infra.database import Database
from src.backend.model.curtida_model import Curtida

class CurtidaRepository:
    @staticmethod
    def create(curtida: Curtida):
        query = """
                INSERT INTO 
                    curtidas (id_user, id_post) 
                VALUES (%s, %s);
                """
        params = (curtida.id_user, curtida.id_post)
        return Database.execute_query(query, params, commit=True)

    @staticmethod
    def get_by_user_post_id(id_user: int, id_post: int):
        query = """
                SELECT 
                    id_user, 
                    id_post 
                FROM 
                    curtidas 
                WHERE 
                    id_user = %s AND id_post = %s;
                """
        result = Database.execute_query(query, (id_user, id_post), fetch_one=True)
        if result:
            return Curtida(**result)
        return None

    @staticmethod
    def get_by_user_id(id_user: int):
        query = """
                SELECT 
                    id_user, 
                    id_post 
                FROM 
                    curtidas 
                WHERE 
                    id_user = %s;
                """
        results = Database.execute_query(query, (id_user,), fetch_all=True)
        return [Curtida(**result) for result in results] if results else []

    @staticmethod
    def get_by_post_id(id_post: int):
        query = """
                SELECT 
                    id_user, 
                    id_post 
                FROM 
                    curtidas 
                WHERE 
                    id_post = %s;
                """
        results = Database.execute_query(query, (id_post,), fetch_all=True)
        return [Curtida(**result) for result in results] if results else []

    @staticmethod
    def get_all():
        query = """
                SELECT 
                    id_user, 
                    id_post 
                FROM 
                    curtidas;
                """
        results = Database.execute_query(query, fetch_all=True)
        return [Curtida(**result) for result in results] if results else []

    @staticmethod
    def delete(id_user: int, id_post: int):
        query = """
                DELETE FROM 
                    curtidas 
                WHERE 
                    id_user = %s AND id_post = %s;
                """
        return Database.execute_query(query, (id_user, id_post), commit=True)

