from dotenv import load_dotenv, find_dotenv
from os import getenv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


found_dotenv = find_dotenv(".env")
load_dotenv(found_dotenv)

__USER = getenv("USER")
__PASSWORD = getenv("PASSWORD")
__DATABASE = getenv("DATABASE")
__HOST = getenv("HOST")
__PORT = getenv("PORT")

class Connection:
    def __init__(self):
        __DATABASE_URL = f"mysql+mysqlconnector://{__USER}:{__PASSWORD}@<{__HOST}:[{__PORT}]/{__DATABASE}"
        engine = create_engine(__DATABASE_URL)

        self._Session = sessionmaker(bind=engine, autoflush=False, autocommit=False)


    def get_db(self):
        db = self._Session()
        try:
            yield db
        except Exception as e:
            raise (e)
        finally:
            db.close()
