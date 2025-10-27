from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.dialects.mysql import VARCHAR, TINYINT, INTEGER


class Base(DeclarativeBase):
    pass


class Status(Base):
    __tablename__ = 'status'

    id: Mapped[int] = mapped_column(INTEGER, primaty_key=True)
    nome: Mapped[str] = mapped_column(VARCHAR(50))
    situacao: Mapped[bool] = mapped_column(TINYINT)

