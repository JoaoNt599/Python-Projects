from flaskr.database import Base
from flaskr.model.codigo_uf import CodigoUF


class Pais(Base, CodigoUF):
    __tablename__ = 'paises'

    def __init__(self, codigo=0, sigla=None, nome=None):
        super(Pais, self).__init__(codigo=codigo, sigla=sigla, nome=nome)