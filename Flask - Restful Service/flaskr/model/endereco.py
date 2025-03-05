from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.schema import UniqueConstraint
from sqlalchemy.orm import relationship
from flaskr.database import Base
from flaskr.model.cidade import Cidade
from flaskr.model.estado import Estado
from flaskr.model.pais import Pais


class Endereco(Base):
    __tablename__ = 'enderecos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    logradouro = Column(String, nullable=False)
    cep = Column(String, nullable=False)
    numero = Column(Integer, nullable=False)
    complemento = Column(String, nullable=True)
    cidade_id = Column(Integer, ForeignKey("cidades.id"), nullable=False)
    cidade = relationship("Cidade", backref="enderecos")
    estado_id = Column(Integer, ForeignKey("estados.id"), nullable=False)
    estado = relationship("Estado", backref="enderecos")
    pais_id = Column(Integer, ForeignKey("paises.id"), nullable=False)
    pais = relationship("Pais", backref="enderecos")
    __table_args__ = (UniqueConstraint('cep', 'numero', name='_cep_numero_uc'),)

    def __init__(self, cep=None, logradouro=None, numero=0,
                 complemento=None, cidade: Cidade = None, estado: Estado = None, pais: Pais = None):
        self.cep = cep
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.cidade = cidade
        self.estado = estado
        self.pais = pais

    def to_dict(self):
        json = {
            "id": self.id,
            "cep": self.cep,
            "logradouro": self.logradouro,
            "numero": self.numero,
            "cidade": self.cidade.to_dict(),
            "estado": self.estado.to_dict(),
            "pais": self.pais.to_dict()
        }

        if self.complemento:
            json["complemento"] = self.complemento

        return json