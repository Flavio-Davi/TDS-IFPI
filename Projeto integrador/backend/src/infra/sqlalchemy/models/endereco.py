from typing import Optional

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR

class Base(DeclarativeBase):
    pass


class Endereco(Base):
    __tablename__ = 'enderecos'

    id: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    rua: Mapped[Optional[str]] = mapped_column(VARCHAR(50))
    bairro: Mapped[Optional[str]] = mapped_column(VARCHAR(50))
    cidade: Mapped[str] = mapped_column(VARCHAR(50))
    estado: Mapped[str] = mapped_column(VARCHAR(50))

