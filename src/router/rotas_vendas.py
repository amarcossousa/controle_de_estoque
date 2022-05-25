from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import get_db
from src.schema import schemas
from src.infra.sqlalchemy.repositorios.repositorio_vendas import RepositorioVendas


router = APIRouter()

@router.post('/venda', status_code=status.HTTP_201_CREATED)
def criar_venda(pd_venda: schemas.Venda, session: Session = Depends(get_db)):
    venda_criada = RepositorioVendas(session).create_venda(pd_venda)
    return venda_criada


