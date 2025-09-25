from .professor import Professor


class Disciplina:
    def __init__(self, codigo: str, nome: str, carga_horaria: int, professor: Professor, descricao= str | None, id_disciplina=None):
        self.__codigo = codigo
        self.__nome = nome
        self.__carga_horaria = carga_horaria
        self.__professor = professor
        self.__descricao = descricao

    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def carga_horaria(self):
        return self.__carga_horaria

    @property
    def professor(self):
        return self.__professor

    @property
    def descricao(self):
        return self.__descricao

    def __str__(self):
        dados = f"Código:{self.codigo},\nNome: {self.nome},\nCarga horária: {self.carga_horaria},\nProfessor: {self.professor},\nDescrição: {self.descricao}" 
        return dados
    
