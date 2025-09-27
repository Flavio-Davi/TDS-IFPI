from pydantic import BaseModel, Field, field_validator
from datetime import date
from ulid import ULID
import re


class Aluno(BaseModel):
    matricula: str = Field(default_factory=lambda: str(ULID()))
    nome_completo: str
    data_nascimento: date
    cpf: str

    @field_validator('cpf', mode='before')
    def validator_cpf(cls, value):
        cpf_clear = re.sub('\D', "", value)
        if len(cpf_clear)!=11:
            raise ValueError('CPF deve ter EXATAMENTE 11 dígitos.')
        return cpf_clear
    
    def __str__(self):
        info = {
            "MATRÍCULA: ": self.matricula,
            "NOME: ": self.nome_completo,
            "DATA DE NASCIMENTO: ": self.data_nascimento,
            "CPF: ": self.cpf
        }
        return str(info)
    