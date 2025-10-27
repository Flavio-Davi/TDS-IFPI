from pydantic import BaseModel
from typing import Optional


class Endereco_create(BaseModel):
    rua: Optional[str] = None
    bairro: Optional[str] = None
    cidade: str
    estado: str


class Endereco_read(Endereco_create):
    id: int

    class Config:
        orm_mode = True
    
class Endereco_update(BaseModel):
    id: int
    rua: Optional[str] = None
    bairro: Optional[str] = None
    cidade: Optional[str] = None
    estado: Optional[str] = None