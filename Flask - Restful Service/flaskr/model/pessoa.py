from sqlalchemy import Column, Integer, Date, String, ForeignKey
from sqlalchemy.schema import UniqueConstraint
from sqlalchemy.orm import relationship
from flaskr.database import Base
from flaskr.model.endereco import Endereco


class Pessoa(Base):
    __tablename__ = 'pessoas'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    cpf = Column(String, nullable=False)
    data_nascimento = Column(Date, nullable=False)
    endereco_id = Column(Integer, ForeignKey("enderecos.id"))
    endereco = relationship("Endereco", backref="pessoas")
    __table_args__ = (UniqueConstraint("cpf"),)

    def __init__(self, nome=None, cpf=None, data_nascimento=None, endereco: Endereco = None):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.endereco = endereco

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'cpf': self.cpf,
            'endereco': self.endereco.to_dict()
        }