from src.backend.model.telefone_model import Telefone
from src.backend.repository.telefone_repository import TelefoneRepository

class TelefoneService:
    @staticmethod
    def criar_telefone(id_user: int, telefone_numero: str):
        if not isinstance(id_user, int) or id_user <= 0:
            return False, "ID de usuário inválido."
        if not telefone_numero or not telefone_numero.strip():
            return False, "Número de telefone não pode ser vazio."
        
        telefone = Telefone(id_user=id_user, telefone=telefone_numero)
        rows_affected = TelefoneRepository.create(telefone)
        if rows_affected > 0:
            return True, "Telefone adicionado com sucesso!"
        return False, "Erro ao adicionar telefone."

    @staticmethod
    def buscar_telefone_por_id(telefone_id: int):
        if not isinstance(telefone_id, int) or telefone_id <= 0:
            return None, "ID de telefone inválido."
        telefone = TelefoneRepository.get_by_id(telefone_id)
        if telefone:
            return telefone, "Telefone encontrado."
        return None, "Telefone não encontrado."

    @staticmethod
    def listar_telefones_por_usuario(id_user: int):
        if not isinstance(id_user, int) or id_user <= 0:
            return [], "ID de usuário inválido."
        telefones = TelefoneRepository.get_by_user_id(id_user)
        return telefones, f"{len(telefones)} telefones encontrados para o usuário {id_user}."

    @staticmethod
    def atualizar_telefone(telefone_id: int, id_user: int, telefone_numero: str):
        if not isinstance(telefone_id, int) or telefone_id <= 0:
            return False, "ID de telefone inválido."
        if not isinstance(id_user, int) or id_user <= 0:
            return False, "ID de usuário inválido."
        if not telefone_numero or not telefone_numero.strip():
            return False, "Número de telefone não pode ser vazio."

        telefone = Telefone(id=telefone_id, id_user=id_user, telefone=telefone_numero)
        rows_affected = TelefoneRepository.update(telefone)
        if rows_affected > 0:
            return True, "Telefone atualizado com sucesso!"
        return False, "Erro ao atualizar telefone ou telefone não encontrado."

    @staticmethod
    def deletar_telefone(telefone_id: int):
        if not isinstance(telefone_id, int) or telefone_id <= 0:
            return False, "ID de telefone inválido."
        rows_affected = TelefoneRepository.delete(telefone_id)
        if rows_affected > 0:
            return True, "Telefone deletado com sucesso!"
        return False, "Erro ao deletar telefone ou telefone não encontrado."

