from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class Chat_participante_create(BaseModel):    
    id_chat: int
    id_usuario: int
    papel: str
    data_entrada: Optional[datetime] = None

class Chat_participante_read(Chat_participante_create):
    class Config:
        orm_mode = True

class Chat_participante_update(BaseModel):
    id_chat: int
    id_usuario: Optional[int] = None
    papel: Optional[str] = None

