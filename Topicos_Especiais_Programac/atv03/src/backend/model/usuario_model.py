from datetime import date

class Usuario:
    def __init__(self, id: int = None, nome_completo: str = None, email: str = None, data_nascimento: date = None):
        self.id = id
        self.nome_completo = nome_completo
        self.email = email
        self.data_nascimento = data_nascimento

    def __repr__(self):
        return f"Usuario(id={self.id}, nome_completo=\'{self.nome_completo}\', email=\'{self.email}\', data_nascimento={self.data_nascimento})"

