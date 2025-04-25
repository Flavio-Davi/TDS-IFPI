import pandas as pd
from sqlalchemy import create_engine

class Data:
    def __init__(self):
        try:
            self.cnx = create_engine("mysql+pymysql://root:Test123@localhost:3306/test")
        except Exception as e:
            print(f"ERROR: {e}")


    def get_data(self):
        return pd.read_sql("SELECT * FROM setor", self.cnx)


    def save_data(self):
        dados = pd.read_sql("SELECT * FROM setor", self.cnx)
        dados.to_excel("dados.xlsx", sheet_name="data_SQL",index=False)
        
        return ">>> Dados salvo com sucesso."


if __name__ == '__main__':
    i = Data()
    print(i.get_data())
