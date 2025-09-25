from ulid import ulid

class Aluno:
    def __init__(self, cpf, nome_completo, data_nascimento):
        self.matricula = ulid()
        self.cpf = cpf
        self.nome_completo = nome_completo
        self.data_nascimento = data_nascimento

    
    def __str__(self):
        dados = f"Nome: {self.nome_completo},\nMatricula: {self.matricula},\nCPF: {self.cpf},\nNascimento: {self.data_nascimento}"
