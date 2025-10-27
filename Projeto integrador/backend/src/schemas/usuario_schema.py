from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime


class Usuario_create(BaseModel):
    id_endereco: int
    id_cargo: int
    id_status: int
    nome: str
    senha: str
    email: str
    data_nascimento: date
    data_criacao: datetime

class Usuario_read(Usuario_create):
    id: int

    class Config:
        orm_mode = True

class Usuario_update(BaseModel):
    id: int
    id_endereco: Optional[int] = None
    id_cargo: Optional[int] = None
    id_status: Optional[int] = None
    nome: Optional[str] = None
    senha: Optional[str] = None
    email: Optional[str] = None
    data_nascimento: Optional[date] = None
    data_criacao: Optional[datetime] = None
    
