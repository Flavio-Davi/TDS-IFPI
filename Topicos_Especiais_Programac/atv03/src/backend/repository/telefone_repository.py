from src.backend.infra.database import Database
from src.backend.model.telefone_model import Telefone

class TelefoneRepository:
    @staticmethod
    def create(telefone: Telefone):
        query = """
                INSERT INTO 
                    telefones (id_user, telefone) 
                VALUES (%s, %s);
                """
        params = (telefone.id_user, telefone.telefone)
        return Database.execute_query(query, params, commit=True)

    @staticmethod
    def get_by_id(telefone_id: int):
        query = """
                SELECT 
                    id, 
                    id_user, 
                    telefone 
                FROM 
                    telefones 
                WHERE 
                    id = %s;
                """
        result = Database.execute_query(query, (telefone_id,), fetch_one=True)
        if result:
            return Telefone(**result)
        return None

    @staticmethod
    def get_by_user_id(user_id: int):
        query = """
                SELECT 
                    id, 
                    id_user, 
                    telefone 
                FROM 
                    telefones 
                WHERE 
                    id_user = %s;
                """
        results = Database.execute_query(query, (user_id,), fetch_all=True)
        return [Telefone(**result) for result in results] if results else []

    @staticmethod
    def get_all():
        query = """
                SELECT 
                    id, 
                    id_user, 
                    telefone 
                FROM 
                    telefones;
                """
        results = Database.execute_query(query, fetch_all=True)
        return [Telefone(**result) for result in results] if results else []

    @staticmethod
    def update(telefone: Telefone):
        query = """
                UPDATE 
                    telefones 
                SET 
                    id_user = %s, 
                    telefone = %s 
                WHERE 
                    id = %s;
                """
        params = (telefone.id_user, telefone.telefone, telefone.id)
        return Database.execute_query(query, params, commit=True)

    @staticmethod
    def delete(telefone_id: int):
        query = """
                DELETE FROM 
                    telefones 
                WHERE 
                    id = %s;
                """
        return Database.execute_query(query, (telefone_id,), commit=True)

