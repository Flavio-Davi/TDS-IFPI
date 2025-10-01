from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy.exc import SQLAlchemyError
from dotenv import load_dotenv
from os import getenv, path


data_env = path.join(path.dirname(__file__), r'.env')
Base = declarative_base()

class Session:
    def __init__(self):
        try:
            load_dotenv(data_env)
            __URL = getenv("URL")
            self.__engine = create_engine(__URL)
            self.__session = sessionmaker(autoflush=False, autocommit=False, bind=self.__engine)
        except SQLAlchemyError as e:
            raise(e)


    def get_session(self):
        return self.__session()
print(data_env)