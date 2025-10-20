# /src/frontend/controller/main_controller.py
from src.backend.service.usuario_service import UsuarioService
from src.backend.service.telefone_service import TelefoneService
from src.backend.service.post_service import PostService
from src.backend.service.comentario_service import ComentarioService
from src.backend.service.curtida_service import CurtidaService
from src.backend.service.amizade_service import AmizadeService
# O model não é estritamente necessário no controller se apenas passamos dados
# from src.backend.model.usuario_model import Usuario

class MainController:
    def __init__(self, view=None):
        self.view = view

    def _show_message(self, result, success_msg="Sucesso", error_msg="Erro"):
        """Função helper para mostrar mensagens na view."""
        data_or_success, message = result
        is_success = bool(data_or_success)
        
        if self.view:
            if is_success:
                self.view.show_message(success_msg, message)
            else:
                self.view.show_message(error_msg, message)
        return data_or_success, message

    # --- Métodos de UsuarioService ---
    def criar_usuario(self, nome_completo, email, data_nascimento):
        result = UsuarioService.criar_usuario(nome_completo, email, data_nascimento)
        return self._show_message(result, "Usuário Criado", "Erro ao Criar")

    def buscar_usuario_por_id(self, user_id):
        result = UsuarioService.buscar_usuario_por_id(user_id)
        return self._show_message(result, "Usuário Encontrado", "Erro ao Buscar")

    def listar_todos_usuarios(self):
        result = UsuarioService.listar_todos_usuarios()
        return self._show_message(result, "Usuários Listados", "Info")

    def atualizar_usuario(self, user_id, nome_completo, email, data_nascimento):
        result = UsuarioService.atualizar_usuario(user_id, nome_completo, email, data_nascimento)
        return self._show_message(result, "Usuário Atualizado", "Erro ao Atualizar")

    def deletar_usuario(self, user_id):
        result = UsuarioService.deletar_usuario(user_id)
        return self._show_message(result, "Usuário Deletado", "Erro ao Deletar")

    # --- Métodos de TelefoneService ---
    def criar_telefone(self, id_user, telefone_numero):
        result = TelefoneService.criar_telefone(id_user, telefone_numero)
        return self._show_message(result, "Telefone Adicionado", "Erro")

    def listar_telefones_por_usuario(self, id_user):
        result = TelefoneService.listar_telefones_por_usuario(id_user)
        return self._show_message(result, "Telefones Encontrados", "Info")

    def atualizar_telefone(self, telefone_id, id_user, telefone_numero):
        result = TelefoneService.atualizar_telefone(telefone_id, id_user, telefone_numero)
        return self._show_message(result, "Telefone Atualizado", "Erro")

    def deletar_telefone(self, telefone_id):
        result = TelefoneService.deletar_telefone(telefone_id)
        return self._show_message(result, "Telefone Deletado", "Erro")

    # --- Métodos de PostService ---
    def criar_post(self, id_user, conteudo, midia=None):
        result = PostService.criar_post(id_user, conteudo, midia)
        return self._show_message(result, "Post Criado", "Erro")

    def buscar_post_por_id(self, post_id):
        result = PostService.buscar_post_por_id(post_id)
        return self._show_message(result, "Post Encontrado", "Erro")

    def listar_posts_por_usuario(self, id_user):
        result = PostService.listar_posts_por_usuario(id_user)
        return self._show_message(result, "Posts Encontrados", "Info")

    def listar_todos_posts(self):
        result = PostService.listar_todos_posts()
        return self._show_message(result, "Posts Listados", "Info")

    def atualizar_post(self, post_id, id_user, conteudo, midia=None):
        result = PostService.atualizar_post(post_id, id_user, conteudo, midia)
        return self._show_message(result, "Post Atualizado", "Erro")

    def deletar_post(self, post_id):
        result = PostService.deletar_post(post_id)
        return self._show_message(result, "Post Deletado", "Erro")

    # --- Métodos de ComentarioService ---
    def criar_comentario(self, id_user, id_post, conteudo):
        result = ComentarioService.criar_comentario(id_user, id_post, conteudo)
        return self._show_message(result, "Comentário Criado", "Erro")

    def listar_comentarios_por_post(self, id_post):
        result = ComentarioService.listar_comentarios_por_post(id_post)
        return self._show_message(result, "Comentários Encontrados", "Info")

    def atualizar_comentario(self, comentario_id, id_user, id_post, conteudo):
        result = ComentarioService.atualizar_comentario(comentario_id, id_user, id_post, conteudo)
        return self._show_message(result, "Comentário Atualizado", "Erro")

    def deletar_comentario(self, comentario_id):
        result = ComentarioService.deletar_comentario(comentario_id)
        return self._show_message(result, "Comentário Deletado", "Erro")

    # --- Métodos de CurtidaService ---
    def curtir_post(self, id_user, id_post):
        result = CurtidaService.curtir_post(id_user, id_post)
        return self._show_message(result, "Post Curtido", "Erro")

    def descurtir_post(self, id_user, id_post):
        result = CurtidaService.descurtir_post(id_user, id_post)
        return self._show_message(result, "Post Descurtido", "Erro")

    def verificar_curtida(self, id_user, id_post):
        result = CurtidaService.verificar_curtida(id_user, id_post)
        return self._show_message(result, "Verificação", "Info")

    def listar_curtidas_por_post(self, id_post):
        result = CurtidaService.listar_curtidas_por_post(id_post)
        return self._show_message(result, "Curtidas Encontradas", "Info")

    # --- Métodos de AmizadeService ---
    def adicionar_amizade(self, user_id_1, user_id_2):
        result = AmizadeService.adicionar_amizade(user_id_1, user_id_2)
        return self._show_message(result, "Amizade Adicionada", "Erro")

    def verificar_amizade(self, user_id_1, user_id_2):
        result = AmizadeService.verificar_amizade(user_id_1, user_id_2)
        return self._show_message(result, "Verificação", "Info")

    def listar_amigos_por_usuario(self, user_id):
        result = AmizadeService.listar_amigos_por_usuario(user_id)
        return self._show_message(result, "Amigos Encontrados", "Info")

    def desfazer_amizade(self, user_id_1, user_id_2):
        result = AmizadeService.desfazer_amizade(user_id_1, user_id_2)
        return self._show_message(result, "Amizade Desfeita", "Erro")
    