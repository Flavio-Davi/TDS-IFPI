from src.backend.model.post_model import Post
from src.backend.repository.post_repository import PostRepository
from datetime import datetime

class PostService:
    @staticmethod
    def criar_post(id_user: int, conteudo: str, midia: str = None):
        if not isinstance(id_user, int) or id_user <= 0:
            return False, "ID de usuário inválido."
        if not conteudo or not conteudo.strip():
            return False, "Conteúdo do post não pode ser vazio."
        
        data_hora_atual = datetime.now()
        post = Post(id_user=id_user, data_hora=data_hora_atual, conteudo=conteudo, midia=midia)
        rows_affected = PostRepository.create(post)
        if rows_affected > 0:
            return True, "Post criado com sucesso!"
        return False, "Erro ao criar post."

    @staticmethod
    def buscar_post_por_id(post_id: int):
        if not isinstance(post_id, int) or post_id <= 0:
            return None, "ID de post inválido."
        post = PostRepository.get_by_id(post_id)
        if post:
            return post, "Post encontrado."
        return None, "Post não encontrado."

    @staticmethod
    def listar_posts_por_usuario(id_user: int):
        if not isinstance(id_user, int) or id_user <= 0:
            return [], "ID de usuário inválido."
        posts = PostRepository.get_by_user_id(id_user)
        return posts, f"{len(posts)} posts encontrados para o usuário {id_user}."

    @staticmethod
    def listar_todos_posts():
        posts = PostRepository.get_all()
        return posts, f"{len(posts)} posts encontrados."

    @staticmethod
    def atualizar_post(post_id: int, id_user: int, conteudo: str, midia: str = None):
        if not isinstance(post_id, int) or post_id <= 0:
            return False, "ID de post inválido."
        if not isinstance(id_user, int) or id_user <= 0:
            return False, "ID de usuário inválido."
        if not conteudo or not conteudo.strip():
            return False, "Conteúdo do post não pode ser vazio."

        existing_post, msg = PostService.buscar_post_por_id(post_id)
        if not existing_post:
            return False, msg

        post = Post(id=post_id, id_user=id_user, data_hora=existing_post.data_hora, conteudo=conteudo, midia=midia)
        rows_affected = PostRepository.update(post)
        if rows_affected > 0:
            return True, "Post atualizado com sucesso!"
        return False, "Erro ao atualizar post ou post não encontrado."

    @staticmethod
    def deletar_post(post_id: int):
        if not isinstance(post_id, int) or post_id <= 0:
            return False, "ID de post inválido."
        rows_affected = PostRepository.delete(post_id)
        if rows_affected > 0:
            return True, "Post deletado com sucesso!"
        return False, "Erro ao deletar post ou post não encontrado."

