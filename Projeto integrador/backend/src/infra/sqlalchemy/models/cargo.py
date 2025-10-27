from src.infra.sqlalchemy.models.empresa import Empresa

from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR


class Base(DeclarativeBase):
    pass


class Cargo(Base):
    __tablename__ = 'cargos'

    id: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    id_empresa: Mapped[int] = mapped_column(INTEGER, ForeignKey('empresas.id'))
    cargo: Mapped[str] = mapped_column(VARCHAR(50))

    empresa: Mapped['Empresa'] = relationship(back_populates='cargos')

    