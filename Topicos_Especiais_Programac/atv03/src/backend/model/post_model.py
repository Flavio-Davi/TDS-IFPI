from datetime import datetime

class Post:
    def __init__(self, id: int = None, id_user: int = None, data_hora: datetime = None, conteudo: str = None, midia: str = None):
        self.id = id
        self.id_user = id_user
        self.data_hora = data_hora
        self.conteudo = conteudo
        self.midia = midia

    def __repr__(self):
        return f"Post(id={self.id}, id_user={self.id_user}, data_hora={self.data_hora}, conteudo=\\'{self.conteudo}\\', midia=\\'{self.midia}\\')"

