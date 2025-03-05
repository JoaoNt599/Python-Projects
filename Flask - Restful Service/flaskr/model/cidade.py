from flaskr.database import Base
from flaskr.model.codigo_uf import CodigoUF


class Cidade(Base, CodigoUF):
    __tablename__ = 'cidades'

    def __init__(self, codigo=0, sigla=None, nome=None):
        super(Cidade, self).__init__(codigo=codigo, sigla=sigla, nome=nome)