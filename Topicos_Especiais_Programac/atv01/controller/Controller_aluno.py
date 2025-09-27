from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from models.model.aluno import Aluno
from models.dao.dao_aluno import DAO_Aluno


router = APIRouter(prefix='/alunos', tags=['Alunos'])
DAO = DAO_Aluno()

@router.post('/', status_code=201)
async def create_aluno(aluno: Aluno):
    dados = DAO.create(aluno)
    return jsonable_encoder(dados)


@router.get('/')
async def read_aluno():
    dados = DAO.read()
    return jsonable_encoder(dados)

@router.get('/{id_aluno}')
async def read_aluno(id_aluno):
    dados = DAO.read(id_aluno)
    return jsonable_encoder(dados)

@router.put('/')
async def update_aluno(aluno: Aluno):
    return "Em produção"

@router.delete('/{id_aluno}')
async def delete__aluno(id_aluno):
    DAO.delete(id_aluno)
