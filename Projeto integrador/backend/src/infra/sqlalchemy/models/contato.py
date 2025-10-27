from src.infra.sqlalchemy.models.usuario import Usuario

from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR

class Base(DeclarativeBase):
    pass


class Contato(Base):
    __tablename__ = 'contatos'

    id: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    id_usuario: Mapped[int] = mapped_column(INTEGER, ForeignKey('usuarios.id'))
    numero: Mapped[str] = mapped_column(VARCHAR(20))

    usuario: Mapped['Usuario'] = relationship(back_populates='contatos')
