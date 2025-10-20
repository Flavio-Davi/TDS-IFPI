from src.backend.model.usuario_model import Usuario
from src.backend.repository.usuario_repository import UsuarioRepository
from datetime import date

class UsuarioService:
    @staticmethod
    def criar_usuario(nome_completo: str, email: str, data_nascimento: str):
        if not nome_completo or not email or not data_nascimento:
            return False, "Todos os campos são obrigatórios."
        
        try:
            data_nascimento_obj = date.fromisoformat(data_nascimento)
        except ValueError:
            return False, "Formato de data de nascimento inválido. Use YYYY-MM-DD."

        usuario = Usuario(nome_completo=nome_completo, email=email, data_nascimento=data_nascimento_obj)
        rows_affected = UsuarioRepository.create(usuario)
        if rows_affected > 0:
            return True, "Usuário criado com sucesso!"
        return False, "Erro ao criar usuário."

    @staticmethod
    def buscar_usuario_por_id(user_id: int):
        if not isinstance(user_id, int) or user_id <= 0:
            return None, "ID de usuário inválido."
        usuario = UsuarioRepository.get_by_id(user_id)
        if usuario:
            return usuario, "Usuário encontrado."
        return None, "Usuário não encontrado."

    @staticmethod
    def listar_todos_usuarios():
        usuarios = UsuarioRepository.get_all()
        return usuarios, f"{len(usuarios)} usuários encontrados."

    @staticmethod
    def atualizar_usuario(user_id: int, nome_completo: str, email: str, data_nascimento: str):
        if not isinstance(user_id, int) or user_id <= 0:
            return False, "ID de usuário inválido."
        if not nome_completo or not email or not data_nascimento:
            return False, "Todos os campos são obrigatórios."
        
        try:
            data_nascimento_obj = date.fromisoformat(data_nascimento)
        except ValueError:
            return False, "Formato de data de nascimento inválido. Use YYYY-MM-DD."

        usuario = Usuario(id=user_id, nome_completo=nome_completo, email=email, data_nascimento=data_nascimento_obj)
        rows_affected = UsuarioRepository.update(usuario)
        if rows_affected > 0:
            return True, "Usuário atualizado com sucesso!"
        return False, "Erro ao atualizar usuário ou usuário não encontrado."

    @staticmethod
    def deletar_usuario(user_id: int):
        if not isinstance(user_id, int) or user_id <= 0:
            return False, "ID de usuário inválido."
        rows_affected = UsuarioRepository.delete(user_id)
        if rows_affected > 0:
            return True, "Usuário deletado com sucesso!"
        return False, "Erro ao deletar usuário ou usuário não encontrado."

