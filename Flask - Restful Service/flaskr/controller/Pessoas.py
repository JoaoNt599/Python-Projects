from flask import Blueprint, request
from flaskr.model.pessoa import Pessoa
from flaskr.model.endereco import Endereco
from flaskr.database import db_session
from datetime import datetime
from sqlalchemy import exc
from re import search
from flaskr.controller.Utils import get_exception_return

from flaskr.controller.RestCommon import index, show, update, delete

pessoas_blueprint = Blueprint('pessoas', __name__)
root_path = '/pessoas'
endereco_field = 'endereco_id'
invalid_date_msg = 'Invalid date format. Expected: YYYYY-MM-DD'


def validate(date_str):
    try:
        date_time_obj = datetime.strptime(date_str, '%Y-%m-%d')
        return {'valid': True, 'date': date_time_obj}
    except:
        return {'valid': False}


@pessoas_blueprint.route(root_path, methods=['GET', 'POST'])
def process_root():
    if request.method == 'GET':
        return index(Pessoa)
    else:
        return create(request)


def create(create):
    data = request.get_json(force=True)
    try:
        nome = data['nome']
        cpf = data['cpf']
        data_nascimento = data['data_nascimento']
        endereco_id = data[endereco_field]
    except:
        return {'message': 'Fields nome, cpf, data_nascimento, endereco_id are required'}, 400

    endereco = Endereco.query.filter_by(id=endereco_id).first()
    if endereco is None:
        return {'message': 'endereco_id not found'}, 404

    date_check = validate_date(data_nascimento)
    if not date_check['valid']:
        return {'message': invalid_date_msg}, 400

    try:
        new_person = Pessoa(nome=nome, cpf=cpf, data_nascimento=date_check['date'], endereco=endereco)
        db_session.add(new_person)
        db_session.commit()
    except exc.IntegrityError as e:
        return_value = get_exception_return()
        if search('UNIQUE constraint failed', str(e)):
            return return_value, 409

        return return_value, 500
    except:
        return get_exception_return(), 500

    return {}, 200


@pessoas_blueprint.route(root_path + '/<id>', methods=['GET', 'PUT', 'DELETE'])
def process_id(id):
    if request.method == 'GET':
        return show(Pessoa, id)
    elif request.method == 'PUT':
        return update_local(id, request)
    elif request.method == 'DELETE':
        return delete(Pessoa, id)


def update_local(id, request):
    data = request.get_json(force=True);
    if endereco_field in data:
        endereco = Endereco.query.filter_by(id=data[endereco_field]).first()
        if endereco is None:
            return {'message': 'endereco_id not found'}, 404

    if 'data_nascimento' in data:
        date_check = validate_date(data['data_nascimento'])
        if not date_check['valid']:
            return {'message': invalid_date_msg}, 400

        data['data_nascimento'] = date_check['date']

    return update(Pessoa, id, request)