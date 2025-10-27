from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class Mensagem_create(BaseModel):
    id_chat: int
    id_remetente: int
    id_destinatario: int
    mensagem: str
    data_envio: Optional[datetime] = None

class Mensagem_read(Mensagem_create):
    id: int
    class Config:
        orm_mode = True

class Mensagem_update(BaseModel):
    id: int
    id_chat: Optional[int] = None
    id_remetente: Optional[int] = None
    id_destinatario: Optional[int] = None
    mensagem: Optional[str] = None

