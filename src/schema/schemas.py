from datetime import datetime
from pydantic import BaseModel
from typing import Optional

class Categorias(BaseModel):
    id : Optional[int] = None
    nome_categoria : str


class Produto(BaseModel):
    id : Optional[int] = None
    nome : str
    quantidade : int
    descricao : str
    tamanho : int
    preco : float
    image : bytes
    ativo : bool
    # categoria : Forenkey de categoria 


class Usuario(BaseModel):
    id : Optional[int] = None
    telefone : str
    cpf : str
    senha : str


class Vendas(BaseModel):
    id : Optional[int] = None
    total : int
    quantidade : int
    preco_unitario : float
    data : Optional[datetime] = None
    
