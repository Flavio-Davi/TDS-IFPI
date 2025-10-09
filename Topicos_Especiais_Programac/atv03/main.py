from models.model.model_usuario import Usuario
from models.dao.dao_usuario import Dao_Usuario

user = Usuario(id=10 ,nome="Daniel", email="daniel2020@gmail.com", data_nascimento="2000-12-21")
dao = Dao_Usuario()


print(dao.update(user))
