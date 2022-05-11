from sqlalchemy import select
from sqlalchemy.orm import Session
from src.schema import schemas
from src.infra.sqlalchemy.models import models

class RepositorioCategorias():


    def __init__(self, session: Session):
        self.session = session
    
    def create_category(self, category: schemas.Categoria):
        session_category = models.Categoria(nome_categoria=category.nome_categoria)
        
        self.session.add(session_category)
        self.session.commit()
        self.session.refresh(session_category)
        return session_category

    def list_category(self):
        category = self.session.query(models.Categoria).all()
        return category
    
    def delete_category(self):
        ...

    def update_category(self):
        ...
    
    def list_caterory_id(self):
        ...