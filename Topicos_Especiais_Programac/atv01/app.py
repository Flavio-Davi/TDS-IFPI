from query import Querie
from datetime import date
from db_config import Conexao

cnx = Conexao()
q = Querie()

# dados = cnx.execute_query_update(q.delete_teacher(), ('13',))
# print(dados)

dados = cnx.execute_query_read(q.read_all_teacher())

for v in dados:
    print(f"""id: {v[0]}
PrimeroNome: {v[1]}
SobreNome: {v[2]}
Matrícula: {v[3]}
Data de Nascimento: {date.strftime(v[4], '%d-%m-%Y')}
E-mail: {v[5]}
""")
    
# 'ctr k c' comentar e 'ctr k u' descomentar
