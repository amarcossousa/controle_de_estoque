from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from src.schema.schemas import Categoria
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repositorios.repositorio_categoria import RepositorioCategorias

router =  APIRouter()


@router.post('/categoria', status_code=status.HTTP_201_CREATED)
def create_category(category: Categoria, session: Session = Depends(get_db) ):
    created_category = RepositorioCategorias(session).create_category(category)
    return created_category

@router.get('/categoria', status_code=status.HTTP_202_ACCEPTED)
def list_category(session: Session = Depends(get_db)):
    lista = RepositorioCategorias(session).list_category()
    return lista