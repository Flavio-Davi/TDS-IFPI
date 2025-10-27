from pydantic import BaseModel
from typing import Optional


class Chats_create(BaseModel):
    id_empresa: int
    nome_chat: Optional[str] = None
    tipo: str
    situacao: bool

class Chats_read(Chats_create):
    id: int

    class Config:
        orm_mode = True

class Chats_update(BaseModel):
    id: int
    id_empresa: Optional[int] = None
    nome_chat: Optional[str] = None
    tipo: Optional[str] = None
    situacao: Optional[bool] = None
