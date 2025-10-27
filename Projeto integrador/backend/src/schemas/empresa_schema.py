from pydantic import BaseModel
from typing import Optional


class Empresa_create(BaseModel):
    id_endereco: int
    id_responsavel: int
    nome_fantasia: str
    cnpj: str
    situacao: bool

class Empresa_read(Empresa_create):
    id: int

    class Config:
        orm_mode = True

class Empresa_update(BaseModel):
    id: int
    id_endereco: Optional[int] = None
    id_responsavel: Optional[int] = None
    nome_fantasia: Optional[str] = None
    cnpj: Optional[str] = None
    situacao: Optional[bool] = None
