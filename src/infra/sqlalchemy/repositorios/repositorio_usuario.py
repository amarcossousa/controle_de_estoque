from fastapi import Depends
from sqlalchemy.orm import Session
from src.schema import schemas
from src.infra.sqlalchemy.models import models
from sqlalchemy import select

class RepositorioUsuarios():


    def __init__(self, session: Session):
        self.session = session
    
    def create_user(self, usuario: schemas.Usuario):
        session_user = models.Usuario(telefone=usuario.telefone,
                                    cpf=usuario.cpf,
                                    senha=usuario.senha)
        self.session.add(session_user)
        self.session.commit()
        self.session.refresh(session_user)
        return session_user

    def delete_user(self):
        ...

    def read_user(self, session: Session):
        read = select(session).where(session == 'usuario')
        result = session.execute(read)
        return result

    
    def upadate_user(self):
        ...

    def read_user_id():
        ...