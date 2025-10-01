from src.infra.config.database import Base
from sqlalchemy import Column, Integer, String


class Model_Cidade(Base):
    __tablename__ = 'cidades'
    id = Column(Integer, primary_key=True, index=True, autoincrement="auto")
    nome_cidade = Column(String)
    estado = Column(String)
    populacao = Column(Integer)
