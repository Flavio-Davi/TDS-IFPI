from src.backend.model.comentario_model import Comentario
from src.backend.repository.comentario_repository import ComentarioRepository
from datetime import datetime

class ComentarioService:
    @staticmethod
    def criar_comentario(id_user: int, id_post: int, conteudo: str):
        if not isinstance(id_user, int) or id_user <= 0:
            return False, "ID de usuário inválido."
        if not isinstance(id_post, int) or id_post <= 0:
            return False, "ID de post inválido."
        if not conteudo or not conteudo.strip():
            return False, "Conteúdo do comentário não pode ser vazio."
        
        data_hora_atual = datetime.now()
        comentario = Comentario(id_user=id_user, id_post=id_post, conteudo=conteudo, data_hora=data_hora_atual)
        rows_affected = ComentarioRepository.create(comentario)
        if rows_affected > 0:
            return True, "Comentário criado com sucesso!"
        return False, "Erro ao criar comentário."

    @staticmethod
    def buscar_comentario_por_id(comentario_id: int):
        if not isinstance(comentario_id, int) or comentario_id <= 0:
            return None, "ID de comentário inválido."
        comentario = ComentarioRepository.get_by_id(comentario_id)
        if comentario:
            return comentario, "Comentário encontrado."
        return None, "Comentário não encontrado."

    @staticmethod
    def listar_comentarios_por_post(id_post: int):
        if not isinstance(id_post, int) or id_post <= 0:
            return [], "ID de post inválido."
        comentarios = ComentarioRepository.get_by_post_id(id_post)
        return comentarios, f"{len(comentarios)} comentários encontrados para o post {id_post}."

    @staticmethod
    def listar_comentarios_por_usuario(id_user: int):
        if not isinstance(id_user, int) or id_user <= 0:
            return [], "ID de usuário inválido."
        comentarios = ComentarioRepository.get_by_user_id(id_user)
        return comentarios, f"{len(comentarios)} comentários encontrados para o usuário {id_user}."

    @staticmethod
    def listar_todos_comentarios():
        comentarios = ComentarioRepository.get_all()
        return comentarios, f"{len(comentarios)} comentários encontrados."

    @staticmethod
    def atualizar_comentario(comentario_id: int, id_user: int, id_post: int, conteudo: str):
        if not isinstance(comentario_id, int) or comentario_id <= 0:
            return False, "ID de comentário inválido."
        if not isinstance(id_user, int) or id_user <= 0:
            return False, "ID de usuário inválido."
        if not isinstance(id_post, int) or id_post <= 0:
            return False, "ID de post inválido."
        if not conteudo or not conteudo.strip():
            return False, "Conteúdo do comentário não pode ser vazio."

        existing_comentario, msg = ComentarioService.buscar_comentario_por_id(comentario_id)
        if not existing_comentario:
            return False, msg

        comentario = Comentario(id=comentario_id, id_user=id_user, id_post=id_post, conteudo=conteudo, data_hora=existing_comentario.data_hora)
        rows_affected = ComentarioRepository.update(comentario)
        if rows_affected > 0:
            return True, "Comentário atualizado com sucesso!"
        return False, "Erro ao atualizar comentário ou comentário não encontrado."

    @staticmethod
    def deletar_comentario(comentario_id: int):
        if not isinstance(comentario_id, int) or comentario_id <= 0:
            return False, "ID de comentário inválido."
        rows_affected = ComentarioRepository.delete(comentario_id)
        if rows_affected > 0:
            return True, "Comentário deletado com sucesso!"
        return False, "Erro ao deletar comentário ou comentário não encontrado."

