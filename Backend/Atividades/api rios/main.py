from fastapi import FastAPI, status
from pydantic import BaseModel


app = FastAPI()

usuarios = {
    1: ["Rio Oiapoque", "Teresina"],
    2: ["Rio Queriniutu", "São Luis"],
    3: ["Rio Amazonas", "Rio de Janeiro"],
    4: ["Rio Jari", "São Paulo"],
    5: ["Rio Xingu", "Fortaleza"],
    6: ["Rio Iriri", "Santa Catarina"]
   }
dados = [value for key, value in usuarios.items()]


class cidade(BaseModel):
    nome: str
    uf: str


@app.get('/cidades', status_code=status.HTTP_200_OK)
def mostrar_dados():
  return dados


@app.post('/create_cidade',  status_code=status.HTTP_201_CREATED)
def criar_usuarios(cidade: cidade):
  return "Cidade criada com sucesso."


@app.put('/cidades/{id_cidade}', status_code=status.HTTP_200_OK)
def update_cidade(id_cidade: int):
   if id_cidade in usuarios.keys():
     return f"Cidade {usuarios[id_cidade][0]} alterada com sucesso"
   else:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Cidade não localizado')
   
  
@app.delete('/cidades/{id_cidade}', status_code=status.HTTP_204_NO_CONTENT)
def delete_rio(id_cidade:int):
  if id_cidade in usuarios.keys():
     return f"Cidade {usuarios[id_cidade][0]} deletada com sucesso."
  else:
     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Cidade não localizado')
