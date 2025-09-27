from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from models.model.professor import Professor
from models.dao.dao_professor import DAO_Professor


router = APIRouter(prefix='/professores', tags=['Professores'])
DAO = DAO_Professor()

@router.post('/', status_code=201)
async def create_disciplina(professor: Professor):
    dados = DAO.create(professor)
    return jsonable_encoder(dados)


@router.get('/')
async def read_disciplina():
    dados = DAO.read()
    return jsonable_encoder(dados)

@router.get('/{id_professor}')
async def read_disciplina(id_professor):
    dados = DAO.read(id_professor)
    return jsonable_encoder(dados)

@router.put('/')
async def update_disciplina(professor: Professor):
    return "Em produção"

@router.delete('/{id_professor}')
async def delete__professor(id_professor):
    DAO.delete(id_professor)
