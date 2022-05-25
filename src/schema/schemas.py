from pydantic import BaseModel
from typing import Optional

class Categoria(BaseModel):
    id : Optional[int] = None
    nome_categoria : str

    class Config:
        orm_mode = True
        

class Produto(BaseModel):
    id : Optional[int] = None
    nome : str
    quantidade : int
    descricao : str
    tamanho : int
    preco : float
    image : bytes
    ativo : bool = False
    categoria : Optional[Categoria]

    class Config:
        orm_mode = True


class UsuarioSimples(BaseModel):
    id : Optional[int] = None
    cpf : str
    
    class Config:
        orm_mode = True

class Usuario(BaseModel):
    id : Optional[int] = None
    telefone : str
    cpf : str
    senha : str

    class Config:
        orm_mode = True


class Venda(BaseModel):
    id : Optional[int] = None
    total : int
    quantidade : int
    preco_unitario : float

    class Config:
        orm_mode = True
    
