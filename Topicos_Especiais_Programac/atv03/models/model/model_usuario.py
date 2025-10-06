class Usuario:
    def __init__(self, nome: str, email: str, data_nascimento: str, id: int | None=None):
        self.id = id
        self.nome = nome
        self.email = self.validar_email(email) 
        self.data_nascimento = data_nascimento


    def validar_email(self, email: str):
        if email.count('@')==1 and email.count('.com')==1:
            return email
        else:
            raise('E-mail inválido, digite um e-mail válido')


    def __str__(self):
        data = {
            'id': self.id,
            'nome': self.nome,
            'email': self.email,
            'data de nascimento': self.data_nascimento
        }
        return str(data)
