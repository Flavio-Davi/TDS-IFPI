from pydantic import BaseModel
from typing import Optional


class Status_create(BaseModel):
    nome: str
    situacao: bool

class Status_read(Status_create):
    id: int

    class Config:
        orm_mode = True

class Status_update(BaseModel):
    id: int
    nome: Optional[str] = None
    situacao: Optional[bool] = None
