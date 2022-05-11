from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from src.schema import schemas
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repositorios.repositorio_usuario import RepositorioUsuarios

router = APIRouter()

@router.post('/usuario')
def create_user(user: schemas.Usuario, session: Session = Depends(get_db)):
    created_user = RepositorioUsuarios(session).create_user(user)
    return created_user

@router.delete('/usuario')
def delete_user():
    pass

@router.put('/usuario')
def update_user():
    pass

@router.get('/usuario')
def read_user_list():
    pass

@router.get('usuario/{id}')
def read_user_id():
    pass

