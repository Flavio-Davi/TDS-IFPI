from models.model.model_usuario import Usuario
from models.dao.dao_usuario import Dao_Usuario

user = Usuario(nome="Vanessa", email="vanessa@gmail.com", data_nascimento="2001-07-11")
dao = Dao_Usuario()

dao.create(user)
print(dao.read())