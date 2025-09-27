from pydantic import BaseModel, EmailStr, field_validator
from typing import Optional, Literal
from datetime import date


class Professor(BaseModel):
    id: Optional[int] | None=None
    nome_completo: str
    matricula: str
    data_nascimento: date
    email: EmailStr
    status: Literal['ATUANDO', 'FÉRIAS', 'LICENÇA', 'INATIVO']    


    @field_validator('status', mode='before')
    @classmethod
    def status_upper(cls, value: str):
        if value is None:
            pass
        elif not isinstance(value, str):
            raise ValueError('Status deve ser uma string válida.')
        return value.upper()

    def __str__(self):
        info = {
                "ID": self.id,
                "NOME": self.nome_completo,
                "MATRÍCULA": self.matricula,
                "DATA DE NASCIMENTO": self.data_nascimento,
                "EMAIL": self.email,
                "ATIVO": self.status
                }
        return str(info)
