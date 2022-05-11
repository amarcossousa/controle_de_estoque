from sqlalchemy import Column, Integer, Float, \
    String, Boolean, DateTime, BigInteger
from src.infra.sqlalchemy.config.database import Base
from sqlalchemy.orm import relationship


class Categoria(Base):
    __tablename__= 'categoria'

    id = Column(Integer, primary_key=True)
    nome_categoria = Column(String)


class Produto(Base):
    __tablename__= 'produto'

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    quantidade = Column(Integer)
    descricao = Column(String)
    tamanho = Column(Integer)
    preco = Column(Float)
    image = Column(BigInteger)
    ativo = Column(Boolean)

    categoria = relationship("Categoria", back_populates="categorias")


class Usuario(Base):
    __tablename__= 'usuario'

    id = Column(Integer, primary_key=True)
    telefone = Column(String)
    cpf = Column(String)
    senha = Column(String)


class venda(Base):
    __tablename__ = 'venda'

    id = Column(Integer, primary_key=True)
    total = Column(Integer)
    quantidade : Column(Integer)
    preco_unitario = Column(Float)
    data = Column(DateTime)




