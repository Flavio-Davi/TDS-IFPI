from fastapi import FastAPI
from fastapi import APIRouter
from http import HTTPStatus
from controller.controlador_Usuario import controle_usuario
from controller.controlador_Usuario import Usuario
from pydantic import BaseModel

app = FastAPI()
router = APIRouter(prefix='/chat')

@router.get('/all', status_code=HTTPStatus.OK)
async def all_chat():
    controller = controle_usuario()
    dados = controller.readme_usuario()
    return dados

class user(BaseModel):
    nome: str
    email: str
    contato: int

@router.put('/create_user', status_code=HTTPStatus.OK)
async def create_user(user: user):
    us = Usuario(user.nome, user.email, user.contato)
    controller = controle_usuario()
    controller.create_usuario(us)
    return 201

app.include_router(router)
