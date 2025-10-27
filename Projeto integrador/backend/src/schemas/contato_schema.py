from pydantic import BaseModel
from typing import Optional


class Contato_create(BaseModel):
    id_usuario: int
    numero: str

class Contato_read(Contato_create):
    id: int

    class Config:
        orm_mode = True

class Contato_update(BaseModel):
    id: int 
    id_usuario: Optional[int] = None
    numero: Optional[str] = None
    