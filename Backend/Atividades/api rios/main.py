from fastapi import FastAPI
from controller.routers_cidade import router as router_cidade 


app = FastAPI()
app.include_router(router_cidade, prefix="/cidades")
