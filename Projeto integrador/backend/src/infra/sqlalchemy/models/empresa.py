from src.infra.sqlalchemy.models.endereco import Endereco
from src.infra.sqlalchemy.models.usuario import Usuario

from typing import Optional

from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR, TINYINT


class Base(DeclarativeBase):
    pass


class Empresa(Base):
    __tablename__ = 'empresas'

    id: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    id_endereco: Mapped[int] = mapped_column(INTEGER, ForeignKey('enderecos.id'))
    id_responsavel: Mapped[Optional[int]] = mapped_column(INTEGER, ForeignKey('usuarios.id'))
    nome_fantasia: Mapped[str] = mapped_column(VARCHAR(100))
    cnpj: Mapped[str] = mapped_column(VARCHAR(50))
    situacao: Mapped[bool] = mapped_column(TINYINT)

    endereco: Mapped['Endereco'] = relationship(back_populates='empresas')
    responsavel: Mapped['Usuario'] = relationship(back_populates='empresas')

