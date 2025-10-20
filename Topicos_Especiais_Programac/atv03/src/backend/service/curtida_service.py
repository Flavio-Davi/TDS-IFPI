from src.backend.model.curtida_model import Curtida
from src.backend.repository.curtida_repository import CurtidaRepository

class CurtidaService:
    @staticmethod
    def curtir_post(id_user: int, id_post: int):
        if not isinstance(id_user, int) or id_user <= 0:
            return False, "ID de usuário inválido."
        if not isinstance(id_post, int) or id_post <= 0:
            return False, "ID de post inválido."
        
        existing_curtida = CurtidaRepository.get_by_user_post_id(id_user, id_post)
        if existing_curtida:
            return False, "Usuário já curtiu este post."

        curtida = Curtida(id_user=id_user, id_post=id_post)
        rows_affected = CurtidaRepository.create(curtida)
        if rows_affected > 0:
            return True, "Post curtido com sucesso!"
        return False, "Erro ao curtir post."

    @staticmethod
    def descurtir_post(id_user: int, id_post: int):
        if not isinstance(id_user, int) or id_user <= 0:
            return False, "ID de usuário inválido."
        if not isinstance(id_post, int) or id_post <= 0:
            return False, "ID de post inválido."
        
        rows_affected = CurtidaRepository.delete(id_user, id_post)
        if rows_affected > 0:
            return True, "Post descurtido com sucesso!"
        return False, "Erro ao descurtir post ou curtida não encontrada."

    @staticmethod
    def verificar_curtida(id_user: int, id_post: int):
        if not isinstance(id_user, int) or id_user <= 0:
            return False, "ID de usuário inválido."
        if not isinstance(id_post, int) or id_post <= 0:
            return False, "ID de post inválido."
        
        curtida = CurtidaRepository.get_by_user_post_id(id_user, id_post)
        if curtida:
            return True, "Usuário curtiu este post."
        return False, "Usuário não curtiu este post."

    @staticmethod
    def listar_curtidas_por_post(id_post: int):
        if not isinstance(id_post, int) or id_post <= 0:
            return [], "ID de post inválido."
        curtidas = CurtidaRepository.get_by_post_id(id_post)
        return curtidas, f"{len(curtidas)} curtidas encontradas para o post {id_post}."

    @staticmethod
    def listar_curtidas_por_usuario(id_user: int):
        if not isinstance(id_user, int) or id_user <= 0:
            return [], "ID de usuário inválido."
        curtidas = CurtidaRepository.get_by_user_id(id_user)
        return curtidas, f"{len(curtidas)} curtidas encontradas pelo usuário {id_user}."

