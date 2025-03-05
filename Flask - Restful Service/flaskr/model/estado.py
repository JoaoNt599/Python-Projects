from flaskr.database import Base
from flaskr.model.codigo_uf import CodigoUF


class Estado(Base, CodigoUF):
    __tablename__ = 'estados'

    def __init__(self, codigo=0, sigla=None, nome=None):
        super(Estado, self).__init__(codigo=codigo, sigla=sigla, nome=nome)