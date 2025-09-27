from fastapi import FastAPI
from controller.Controller_aluno import router as aluno
from controller.Controller_disciplina import router as disciplina
from controller.Controller_professor import router as professor

app = FastAPI()
app.include_router(aluno, prefix='/escola')
app.include_router(disciplina, prefix='/escola')
app.include_router(professor, prefix='/escola')


@app.get('/')
async def home():
    return "Está funcionando."
