from query import Querie
from datetime import date
from db_config import Conexao

cnx = Conexao()

#dt = date(1983, 1, 28)
#q = Querie().insert_data()
#up = cnx.execute_long_query(q, ('Sandy', 'Junior', 'SALO2025SP', dt, 'sandyjr@gmail.com'))

cnx_data = Conexao()
dados = cnx_data.execute_query(Querie().all_data())

for dado in dados:
    print({
        "ID": f"{dado[0]}",
        "PRIMEIRO_NOME": f"{dado[1]}",
        "SOBRE_NOME": f"{dado[2]}",
        "MATRICULA": f"{dado[3]}",
        "DATA_NASCIMENTO": f"{date.strftime(dado[4], "%d/%m/%Y")}",
        "E-MAIL": f"{dado[5]}"
    })
  
