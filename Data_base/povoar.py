import pandas as pd
from sqlalchemy import engine

class Povoar:
    def __init__(self):
        try:
            self._cnx = "mysql+pymysql://root:mysql123@127.0.0.1/PUBLICACOES"
        except:
            print(">> Erro ao conectar com o banco de dados.")    


    @property
    def cnx(self):
        return self._cnx


    def send(self, data: pd.DataFrame):
        try:
            data.to_sql("NACIONALIDADE", self.cnx, if_exists="append", index=False)
            return print("Sucesso ao inserir os dados.")
        except Exception as e:
            return print(f"ERROR: {e}")


def main():
    i = Povoar()
    data = pd.read_excel("./data.xlsx", dtype={"ID": int, "NC": str})
    i.send(data)


if __name__ == '__main__':
    main()
