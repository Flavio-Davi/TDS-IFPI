from datetime import date, datetime

from src.infra.sqlalchemy.models.contato import Contato
from src.infra.sqlalchemy.models.endereco import Endereco
from src.infra.sqlalchemy.models.cargo import Cargo
from src.infra.sqlalchemy.models.status import Status

from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.dialects.mysql import VARCHAR, INTEGER, DATE, DATETIME


class Base(DeclarativeBase):
    pass


class Usuario(Base):
    __tablename__ = 'usuarios'

    id: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    id_endereco: Mapped[int] = mapped_column(INTEGER, ForeignKey('enderecos.id'))
    id_cargo: Mapped[int] = mapped_column(INTEGER, ForeignKey('cargos.id'))
    id_status: Mapped[int] = mapped_column(INTEGER, ForeignKey('status.id'))
    nome: Mapped[str] = mapped_column(VARCHAR(255))
    senha: Mapped[str] = mapped_column(VARCHAR(255))
    email: Mapped[str] = mapped_column(VARCHAR(100))
    data_nascimento: Mapped[date] = mapped_column(DATE)
    data_criacao: Mapped[datetime] = mapped_column(DATETIME)

    endereco: Mapped['Endereco'] = relationship(back_populates='usuarios')
    cargo: Mapped[Cargo] = relationship(back_populates='usuarios')
    status: Mapped['Status'] = relationship(back_populates='usuarios')

