from datetime import date

class BaseUser:
    def __init__(self, nome: str, email: str, data_nascimento: date):
        self.nome = nome
        self.email = self.validar_email(email)
        self.data_nascimento = data_nascimento


    def validar_email(self, email: str):
        if email.count('@')==1 and email.count('.')<1:
            return email
        else:
            raise ValueError('E-mail inválido, digite um e-mail válido')


    def __str__(self):
        data = {
            'nome': self.nome,
            'email': self.email,
            'data de nascimento': self.data_nascimento.strftime('%d/%m/%Y')
        }
        return str(data)
    

class CreateUser(BaseUser):
    pass


class UpdateUser(BaseUser):
    def __init__(self, id: int):
        super().__init__()
        self.id = id