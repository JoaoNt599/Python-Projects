from flask_seeder import Seeder
from flaskr.database import db
from datetime import date
from flaskr.model.pessoa import Pessoa
from flaskr.model.endereco import Endereco
from flaskr.model.cidade import Cidade
from flaskr.model.estado import Estado
from flaskr.model.pais import Pais


class PessoaSeeder(Seeder):
    def run(self):
        cidade1 = Cidade(codigo=1, sigla="LW", nome="Little Whinging")
        estado1 = Estado(codigo=1, sigla="SU", nome="Surrey")
        pais1 = Pais(codigo=1, sigla="UK", nome="United Kingdom")
        endereco1 = Endereco(cep="22793220",  logradouro="Privet Drive", numero="4", complemento="",
                             cidade=cidade1, estado=estado1, pais=pais1)
        pessoa1 = Pessoa(nome="The Dursleys", cpf="35681193071", data_nascimento=date(1988, 1, 1), endereco=endereco1)

        cidade2 = Cidade(codigo=2, sigla="MET", nome="Metropolis")
        estado2 = Estado(codigo=2, sigla="FL", nome="Delaware")
        pais2 = Pais(codigo=2, sigla="DL", nome="Estados Unidos")
        endereco2 = Endereco(cep="3465798",  logradouro="Clinton St", numero="344", complemento="Apt 3B",
                             cidade=cidade2, estado=estado2, pais=pais2)
        pessoa2 = Pessoa(nome="Clark Kent", cpf="45678912321", data_nascimento=date(1980, 2, 2), endereco=endereco2)

        cidade3 = Cidade(codigo=3, sigla="CHD", nome="Chongwen District")
        estado3 = Estado(codigo=3, sigla="BJ", nome="Beijing")
        pais3 = Pais(codigo=3, sigla="CN", nome="China")
        endereco3 = Endereco(cep="9658741",  logradouro="Yi Ceng 84hao", numero="344", complemento="Apt 3B",
                             cidade=cidade3, estado=estado3, pais=pais3)
        pessoa3 = Pessoa(nome="Ye Wenjie", cpf="32111256476", data_nascimento=date(1960, 4, 4), endereco=endereco3)

        db.session.add_all([pessoa1, pessoa2, pessoa3])
        db.session.commit()
        db.session.close()