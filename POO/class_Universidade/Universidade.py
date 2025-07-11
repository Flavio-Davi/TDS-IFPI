class Universidade:
  _alunos_publicas = []
  
  def __init__(self,nome,tipo):
    self.__nome = nome
    self.__tipo = tipo
    self.__alunos = []

  def matricular(self,aluno):
       if isinstance(aluno, Aluno):
            if self.__tipo == 1:
                for aluno_publico in Universidade._alunos_publicas:
                    if aluno_publico.cpf == aluno.cpf:
                        return False
                
                Universidade._alunos_publicas.append(aluno)
            
            self.__alunos.append(aluno)
            return True
       return False

  def remover(self,aluno):
    self.__alunos.remove(aluno)
    
    if self.__tipo == 1:
        Universidade._alunos_publicas.remove(aluno)

  def listar(self):
    print(f'=== Alunos Matriculados na {self.__nome} ======:')
    for aluno in self.__alunos:
      print(aluno.nome)

  @property
  def alunos(self):
    return self.__alunos

  @property
  def nome(self):
    return self.__nome

  @property
  def tipo(self):
    return self.__tipo


class Aluno:
  def __init__(self,nome,cpf,matricula):
    self.__nome = nome
    self.__cpf = cpf
    self.__matricula = matricula

  @property
  def nome(self):
    return self.__nome

  @property
  def matricula(self):
    return self.__matricula
  
  @property
  def cpf(self):
    return self.__cpf


UFPI = Universidade("UFPI",1)
UESPI = Universidade("UESPI",1)
FACID = Universidade("FACID",2)

maria = Aluno("Maria","021524874-65",123456)
joao = Aluno("João","021524874-65",654321)

print(f"Matrícula Maria na UFPI: {UFPI.matricular(maria)}")
print(f"Matrícula João na UESPI: {UESPI.matricular(joao)}")
print(f"Matrícula João na FACID: {FACID.matricular(joao)}")

UFPI.listar()
UESPI.listar()
FACID.listar()
