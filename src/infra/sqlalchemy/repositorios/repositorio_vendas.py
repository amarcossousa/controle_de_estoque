from src.schema import schemas 
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.models import models


class RepositorioVendas():

    def __init__(self, session: Session):
        self.session = session

    def create_venda(self, venda: schemas.Venda):
        criar_venda = models.Venda(total=venda.total,
                                    quantidade=venda.quantidade,
                                    preco_unitario=venda.preco_unitario,
                                    data=venda.data)
        self.session.add(criar_venda)
        self.session.commit()
        self.session.refresh(criar_venda)
        return criar_venda

    def update_venda(self):
        pass

    def remove_venda(self):
        pass

    def listar_veda(self):
        pass




