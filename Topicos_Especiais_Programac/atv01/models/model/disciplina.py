from pydantic import BaseModel
from typing import Optional
from models.model.professor import Professor


class Disciplina(BaseModel):
    id: int
    codigo: str
    nome: str
    descricao: str
    id_professor: Optional[int] | None=None
    carga_horaria: int


    def __str__(self):
        info = {
            "ID: ": self.id,
            "CÓDIGO: ": self.codigo,
            "NOME: ": self.nome,
            "DESCRIÇÃO: ": self.descricao,
            "ID PROFESSOR: ": self.id_professor,
            "CARGA HORÁRIA: ": self.carga_horaria
        }
        return str(info)
