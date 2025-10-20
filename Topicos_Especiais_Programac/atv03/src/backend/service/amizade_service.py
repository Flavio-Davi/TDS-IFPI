from src.backend.model.amizade_model import Amizade
from src.backend.repository.amizade_repository import AmizadeRepository
from datetime import datetime

class AmizadeService:
    @staticmethod
    def adicionar_amizade(user_id_1: int, user_id_2: int):
        if not isinstance(user_id_1, int) or user_id_1 <= 0 or not isinstance(user_id_2, int) or user_id_2 <= 0:
            return False, "IDs de usuário inválidos."
        if user_id_1 == user_id_2:
            return False, "Não é possível adicionar a si mesmo como amigo."
        
        existing_amizade = AmizadeRepository.get_by_users_id(user_id_1, user_id_2)
        if existing_amizade:
            return False, "Amizade já existe."

        data_hora_atual = datetime.now()
        amizade = Amizade(user_id=user_id_1, user_id_02=user_id_2, data_hora=data_hora_atual)
        rows_affected = AmizadeRepository.create(amizade)
        if rows_affected > 0:
            return True, "Amizade adicionada com sucesso!"
        return False, "Erro ao adicionar amizade."

    @staticmethod
    def verificar_amizade(user_id_1: int, user_id_2: int):
        if not isinstance(user_id_1, int) or user_id_1 <= 0 or not isinstance(user_id_2, int) or user_id_2 <= 0:
            return False, "IDs de usuário inválidos."
        amizade = AmizadeRepository.get_by_users_id(user_id_1, user_id_2)
        if amizade:
            return True, "Amizade existe."
        return False, "Amizade não existe."

    @staticmethod
    def listar_amigos_por_usuario(user_id: int):
        if not isinstance(user_id, int) or user_id <= 0:
            return [], "ID de usuário inválido."
        amizades = AmizadeRepository.get_all_by_user_id(user_id)
        amigos_ids = []
        for amizade in amizades:
            if amizade.user_id == user_id:
                amigos_ids.append(amizade.user_id_02)
            else:
                amigos_ids.append(amizade.user_id)
        return amigos_ids, f"{len(amigos_ids)} amigos encontrados para o usuário {user_id}."

    @staticmethod
    def desfazer_amizade(user_id_1: int, user_id_2: int):
        if not isinstance(user_id_1, int) or user_id_1 <= 0 or not isinstance(user_id_2, int) or user_id_2 <= 0:
            return False, "IDs de usuário inválidos."
        rows_affected = AmizadeRepository.delete(user_id_1, user_id_2)
        if rows_affected > 0:
            return True, "Amizade desfeita com sucesso!"
        return False, "Erro ao desfazer amizade ou amizade não encontrada."

