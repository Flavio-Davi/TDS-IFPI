from fastapi import APIRouter
from models.cidade import Cidade
from models.cidade import DAO_Cidade


router = APIRouter()

@router.post('/create', status_code=201)
def create_city(cidade: Cidade):
    DAO = DAO_Cidade()
    criado = DAO.create_city(cidade)
    return criado
