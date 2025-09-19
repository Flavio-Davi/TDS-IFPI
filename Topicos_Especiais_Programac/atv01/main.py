from fastapi import FastAPI
from controller.Controller_Aluno import router

app = FastAPI()
app.include_router(router)


@app.get('/escola')
async def escola_home():
    return "Está funcionando."
