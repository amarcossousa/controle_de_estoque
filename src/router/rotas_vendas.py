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

@router.get('/vendas', status_code=status.HTTP_202_ACCEPTED) # deve receber apenas as vendas de cada usuario logado ou por ID
def list_vendas(session: Session = Depends(get_db)):
    lista_vendas = RepositorioVendas(session).listar_venda()
    return lista_vendas

@router.delete('/venda/{id}', status_code=status.HTTP_202_ACCEPTED)
def remover_venda(id: int, session: Session =Depends(get_db)):
    removido = RepositorioVendas(session).remove_venda(id)
    return removido