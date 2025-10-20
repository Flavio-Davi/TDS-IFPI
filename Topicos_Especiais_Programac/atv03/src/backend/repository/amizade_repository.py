from src.backend.infra.database import Database
from src.backend.model.amizade_model import Amizade

class AmizadeRepository:
    @staticmethod
    def create(amizade: Amizade):
        query = """
                INSERT INTO 
                    amizade (user_id, user_id_02, data_hora) 
                VALUES (%s, %s, %s);
                """
        params = (amizade.user_id, amizade.user_id_02, amizade.data_hora)
        return Database.execute_query(query, params, commit=True)
 
    @staticmethod
    def get_by_users_id(user_id_1: int, user_id_2: int):
        query = """
                SELECT 
                    user_id, 
                    user_id_02, 
                    data_hora 
                FROM 
                    amizade 
                WHERE 
                    (user_id = %s AND user_id_02 = %s) 
                OR 
                    (user_id = %s AND user_id_02 = %s);
                """
        result = Database.execute_query(query, (user_id_1, user_id_2, user_id_2, user_id_1), fetch_one=True)
        if result:
            return Amizade(**result)
        return None

    @staticmethod
    def get_all_by_user_id(user_id: int):
        query = """
                SELECT 
                    user_id, 
                    user_id_02, 
                    data_hora 
                FROM 
                    amizade 
                WHERE 
                    user_id = %s OR user_id_02 = %s;
                """
        results = Database.execute_query(query, (user_id, user_id), fetch_all=True)
        return [Amizade(**result) for result in results] if results else []

    @staticmethod
    def get_all():
        query = """
                SELECT 
                    user_id, 
                    user_id_02, 
                    data_hora 
                FROM 
                    amizade;
                """
        results = Database.execute_query(query, fetch_all=True)
        return [Amizade(**result) for result in results] if results else []

    @staticmethod
    def delete(user_id_1: int, user_id_2: int):
        query = """
                DELETE FROM 
                    amizade 
                WHERE 
                    (user_id = %s AND user_id_02 = %s) 
                OR 
                    (user_id = %s AND user_id_02 = %s);
                """
        return Database.execute_query(query, (user_id_1, user_id_2, user_id_2, user_id_1), commit=True)

