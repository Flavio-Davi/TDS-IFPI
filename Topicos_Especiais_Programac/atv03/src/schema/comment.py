from datetime import datetime


class BaseComment:
    def __init__(self, conteudo: str, data_hora: datetime):
        self.conteudo = conteudo
        self.data_hora = data_hora


    def __str__(self):
        data = {
            'conteudo': self.conteudo,
            'data_hora': self.data_hora
        }
        return data


class CreateComment(BaseComment):
    pass


class UpdateComment(BaseComment):
    def __init__(self, id: int):
        super().__init__()
        self.id = id
