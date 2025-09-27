from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from models.model.disciplina import Disciplina
from models.dao.dao_disciplina import DAO_Disciplina


router = APIRouter(prefix='/disciplinas', tags=['Disciplinas'])
DAO = DAO_Disciplina()

@router.post('/', status_code=201)
async def create_disciplina(disciplina: Disciplina):
    dados = DAO.create(disciplina)
    return jsonable_encoder(dados)


@router.get('/')
async def read_disciplina():
    dados = DAO.read()
    return jsonable_encoder(dados)

@router.get('/{id_disciplina}')
async def read_disciplina(id_disciplina):
    dados = DAO.read(id_disciplina)
    return jsonable_encoder(dados)

@router.put('/')
async def update_disciplina(disciplina: Disciplina):
    return "Em produção"

@router.delete('/{id_disciplina}')
async def delete__disciplina(id_disciplina):
    DAO.delete(id_disciplina)
