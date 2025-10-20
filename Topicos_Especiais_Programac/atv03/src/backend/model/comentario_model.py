from datetime import datetime

class Comentario:
    def __init__(self, id: int = None, id_user: int = None, id_post: int = None, conteudo: str = None, data_hora: datetime = None):
        self.id = id
        self.id_user = id_user
        self.id_post = id_post
        self.conteudo = conteudo
        self.data_hora = data_hora

    def __repr__(self):
        return f"Comentario(id={self.id}, id_user={self.id_user}, id_post={self.id_post}, conteudo=\\'{self.conteudo}\\', data_hora={self.data_hora})"

