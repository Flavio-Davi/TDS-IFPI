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

    @p_nome.setter
    def p_nome(self, new_p_nome):
        self.__p_nome = new_p_nome

    @s_nome.setter
    def s_nome(self, new_s_nome):
        self.__s_nome = new_s_nome

    @matricula.setter
    def matricula(self, new_matricula):
        self.__matricula = new_matricula

    @data_nascimento.setter
    def data_nascimento(self, new_data_nascimento):
        self.__data_nascimento = new_data_nascimento

    @email.setter
    def email(self, new_email):
        self.__email = new_email
