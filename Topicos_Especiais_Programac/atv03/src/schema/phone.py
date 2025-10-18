class BasePhone:
    def __init__(self, telefone: str):
        self.telefone = telefone

    def __str__(self) -> str:
        data = {
            'telefone': self.telefone
        }
        return str(data)
    

class CreatePhone(BasePhone):
    pass


class UpdatePhone(BasePhone):
    def __init__(self, id = None, id_user = None):
        super().__init__()
        self.id = id
        self.id_user = id_user

        