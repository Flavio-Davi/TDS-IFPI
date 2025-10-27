from datetime import datetime

from src.infra.sqlalchemy.models.usuario import Usuario
from src.infra.sqlalchemy.models.chats import Chats

from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.dialects.mysql import INTEGER, TEXT, DATETIME


class Base(DeclarativeBase):
    pass

class Mensagem(Base):
    __tablename__ = 'mensagens'

    id: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    id_chat: Mapped[int] = mapped_column(INTEGER, ForeignKey('chats.id'))
    id_remetente: Mapped[int] = mapped_column(INTEGER, ForeignKey('usuarios.id'))
    id_remetente: Mapped[int] = mapped_column(INTEGER, ForeignKey('usuarios.id'))
    mensagem: Mapped[str] = mapped_column(TEXT)
    data_envio: Mapped[datetime] = mapped_column(DATETIME)


# id int AI PK 
# id_chat int 
# id_remetente int 
# id_destinatario int 
# mensagem text 
# data_envio timestamp