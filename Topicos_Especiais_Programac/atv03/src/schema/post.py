from datetime import datetime

class BasePost:
    def __init__(self, data_hora: datetime, conteudo: str, midia: str | None=None):
        self.data_hora = data_hora
        self.conteudo = conteudo
        self.midia = midia

    def __str__(self) -> str:
        data = {
            'data_hora': self.data_hora,
            'conteudo': self.conteudo,
            'midia': self.midia
        }
        return str(data)


class CreatePost(BasePost):
    pass


class UpdatePost(BasePost):
    def __init__(self, id: int, id_user: int):
        super().__init__()
        self.id = id
        self.id_user = id_user

