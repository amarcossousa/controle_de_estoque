from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from src.schema.schemas import Usuario, UsuarioSimples
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repositorios.repositorio_usuario import RepositorioUsuarios
from typing import List
router = APIRouter()

@router.post('/usuario')
def create_user(user: Usuario, session: Session = Depends(get_db)):
    created_user = RepositorioUsuarios(session).create_user(user)
    return created_user

@router.delete('/usuario')
def delete_user():
    pass

@router.put('/usuario')
def update_user():
    pass

@router.get('/usuario', status_code=status.HTTP_202_ACCEPTED, response_model=List[UsuarioSimples])
def read_user_list(session: Session = Depends(get_db)):
    list_user = RepositorioUsuarios(session).read_user()
    return list_user

@router.get('usuario/{id}')
def read_user_id():
    pass

