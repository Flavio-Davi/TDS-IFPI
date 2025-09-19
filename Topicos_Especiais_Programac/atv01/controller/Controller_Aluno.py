from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from models.aluno import Aluno
from models.aluno import DAO_Aluno


router = APIRouter(prefix='/alunos')


@router.post('/', status_code=201)
async def create_aluno(aluno: Aluno):
    DAO = DAO_Aluno()
    return DAO.create(aluno)

@router.get('/')
async def read_aluno(aluno: Aluno | None=None):
    DAO = DAO_Aluno()
    if aluno:
        dados = DAO.read(aluno)
    else:
        dados = DAO.read()
    return jsonable_encoder(dados)

