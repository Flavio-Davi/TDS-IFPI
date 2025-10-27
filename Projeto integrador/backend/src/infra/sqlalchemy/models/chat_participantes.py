from datetime import datetime

from src.infra.sqlalchemy.models.chats import Chats
from src.infra.sqlalchemy.models.usuario import Usuario

from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.dialects.mysql import INTEGER, ENUM, DATETIME

class Base(DeclarativeBase):
    pass


class Chat_participantes(Base):
    __tablename__ = 'chat_participantes'

    id_chat: Mapped[int] = mapped_column(INTEGER, ForeignKey('chats.id'))
    id_usuario: Mapped[int] = mapped_column(INTEGER, ForeignKey('usuarios.id'))
    papel: Mapped[int] = mapped_column(ENUM('administrador', 'membro'))
    data_entrada: Mapped[datetime] = mapped_column(DATETIME)

    chat: Mapped['Chats'] = relationship(back_populates='chat_participantes')
    usuario: Mapped['Usuario'] = relationship(back_populates='chat_participantes')

