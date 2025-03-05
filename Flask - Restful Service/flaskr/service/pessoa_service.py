from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound
from flaskr.database import db
from flaskr.model.pessoa import Pessoa
from flask import jsonify, make_response


def obter_pessoa_pelo_cpf(cpf: str):
    try:
        pessoa = db.session.query(Pessoa).filter(Pessoa.cpf == cpf).one()
        response = make_response(jsonify(pessoa.to_dict()))
        response.headers['Content-Type'] = 'application/json'
        return response
    except MultipleResultsFound:
        raise
    except NoResultFound:
        raise