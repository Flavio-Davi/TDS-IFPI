from src.infra.config.database import Session
from src.infra.models.model_cidade import Model_Cidade


class Repositorio_Cidade:
    def __init__(self, db_session: Session):
        self.__cnx = db_session.get_session()

    
    def create(self, cidade: Model_Cidade):
        data_city = Model_Cidade(nome_cidade=cidade.nome_cidade,
                                 estado=cidade.estado,
                                 populacao=cidade.populacao)
        self.__cnx.add(data_city)
        self.__cnx.commit()
        self.__cnx.refresh(data_city)
        return data_city


    def read(self):
        cidades = self.__cnx.query(Model_Cidade).all()
        return cidades
    

    def update(self):
        pass
    def delete(self):
        pass
