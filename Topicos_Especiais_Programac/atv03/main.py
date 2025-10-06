from models.model.model_usuario import Usuario
from models.dao.dao_usuario import Dao_Usuario

user = Usuario(nome="Flavio", email="flavio@gmail.com", data_nascimento="1999-21-04")
dao = Dao_Usuario()

dao.create(user)
print(dao.read())