class Telefone:
    def __init__(self, id: int = None, id_user: int = None, telefone: str = None):
        self.id = id
        self.id_user = id_user
        self.telefone = telefone

    def __repr__(self):
        return f"Telefone(id={self.id}, id_user={self.id_user}, telefone='{self.telefone}')"

