from sqlalchemy import Column, Integer, String


class CodigoUF(object):
    id = Column(Integer, primary_key=True, autoincrement=True)
    codigo = Column(Integer, nullable=False)
    sigla = Column(String, nullable=False)
    nome = Column(String, nullable=False)

    # Ver 'problema do diamante'
    # **kwargs - parâmetros nomeados
    def __init__(self, **kwargs):
        self.codigo = kwargs['codigo']
        self.sigla = kwargs['sigla']
        self.nome = kwargs['nome']

    def to_dict(self):
        return {
            "id": self.id,
            "codigo": self.codigo,
            "sigla": self.sigla,
            "nome": self.nome
        }