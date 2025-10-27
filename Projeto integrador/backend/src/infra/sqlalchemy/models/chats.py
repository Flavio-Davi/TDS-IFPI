from src.infra.sqlalchemy.models.empresa import Empresa

from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR, ENUM, TINYINT

class Base(DeclarativeBase):
    pass


class Chats(Base):
    __tablename__ = 'chats'

    id: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    id_empresa: Mapped[int] = mapped_column(INTEGER, ForeignKey('empresas.id'))
    nome: Mapped[str] = mapped_column(VARCHAR(255))
    tipo: Mapped[str] = mapped_column(ENUM('privada', 'grupo'))
    situacao: Mapped[bool] = mapped_column(TINYINT)

    empresa: Mapped['Empresa'] = relationship(back_populates='chats')

