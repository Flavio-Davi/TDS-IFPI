from dotenv import load_dotenv
from pathlib import Path
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Meta_data:
    def __init__(self):
        dir_meta = Path(__file__).parents
        #load_dotenv(dir_meta)
        self.__USER = getenv('USER')
        self.__PASSWORD = getenv('PASSWORD')
        self.__DATABASE = getenv('DATABASE')
        self.__PORT = getenv('PORT')
        self.__HOST = getenv('HOST')


class Conexao(Meta_data):
    def __init__(self):
        super().__init__()
        self.__engine = create_engine(f'mysql+mysqlconnector://root:mysql123@127.0.0.1:3306/glr_volei')
        self.session = sessionmaker(bind=self.__engine, autoflush=False, autocommit=False)


    def get_db(self):
        db = self.session()
        try:
            yield db
        finally:
            db.close()
