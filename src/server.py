from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.router import rotas_usuarios, rotas_categorias
from src.infra.sqlalchemy.config.database import criar_db

criar_db()

app = FastAPI()

origins = [
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rotas usuarios
app.include_router(rotas_usuarios.router)
# Rotas categorias
app.include_router(rotas_categorias.router)



