from datetime import date

class Professor:
    def __init__(self, p_nome: str, s_nome: str, matricula: str, data_nascimento: date, email: str):
        self.__p_nome = p_nome
        self.__s_nome = s_nome
        self.__matricula = matricula
        self.__data_nascimento = data_nascimento
        self.__email = email

    @property
    def p_nome(self):
        return self.__p_nome

    @property
    def s_nome(self):
        return self.__s_nome

    @property
    def matricula(self):
        return self.__matricula
    
    @property
    def data_nascimento(self):
        return self.__data_nascimento

    @property
    def email(self):
        return self.__email

    def __str__(self):
        dados = f"Nome: {self.p_nome},\nSobrenome: {self.s_nome},\nMatrícula: {self.matricula},\nNascimento: {self.data_nascimento},\nE-mail: {self.email}"
        
