import pandas as pd
from sqlalchemy import engine

class Povoar:
    def __init__(self, user: str, password: str, host: str, db_name: str):
        try:
            self._engine = engine.create_engine(f"mysql+pymysql://{user}:{password}@{host}/{db_name}")
            print("Conexão estabelecida com sucesso.")
        except Exception as e:
            raise e
    

    @property
    def engine(self):
        return self._engine


    def send(self, data: pd.DataFrame, name_table: str):
        try:
            data.to_sql(f"{name_table}", self.engine, if_exists="append", index=False)
            print("Dados inserido com sucesso no banco de dados")
        except Exception as e:
            raise e


def main():
    data = r".\data_nacionalidade.csv"
    i  = Povoar()


if __name__ == '__main__':
    main()
