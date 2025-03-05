from flask import Blueprint, request
from flaskr.controller.Utils import get_exception_return, check_entity_presence
from flaskr.models import Endereco, Pais, Cidade, Estado
from flaskr.database import db_session
from sqlalchemy import exc
from re import search

from flaskr.controller.RestCommon import index, show, update, delete

enderecos_blueprint = Blueprint('enderecos', __name__)
root_path = '/enderecos'
cidade_field = 'cidade_id'
estado_field = 'estado_id'
pais_field = 'pais_id'


@enderecos_blueprint.route(root_path, methods=['GET', 'POST'])
def process_root():
    if request.method == 'GET':
        return index(Endereco)
    else:
        return create(request)


def create(create):
    data = request.get_json(force=True)
    try:
        logradouro = data['logradouro']
        numero = data['numero']
        cep = data['cep']
        cidade_id = data[cidade_field]
        estado_id = data[estado_field]
        pais_id = data[pais_field]
    except:
        return {'message': 'Fields logradouro, numero, cep, cidade_id, estado_id, pais_id are required'}, 400

    complemento = None
    if 'complemento' in data:
        complemento = data['complemento']

    not_found = []
    cidade = Cidade.query.filter_by(id=cidade_id).first()
    if cidade is None:
        not_found.append(cidade_field)

    estado = Estado.query.filter_by(id=estado_id).first()
    if estado is None:
        not_found.append(estado_field)

    pais = Pais.query.filter_by(id=pais_id).first()
    if pais is None:
        not_found.append(pais_field)

    if not_found:
        return {'message': 'Following fields not found: ' + ', '.join(not_found)}, 404

    try:
        new_address = Endereco(cep=cep, logradouro=logradouro, numero=numero, complemento=complemento, cidade=cidade,
                               estado=estado, pais=pais)
        db_session.add(new_address)
        db_session.commit()
    except exc.IntegrityError as e:
        return_value = get_exception_return()
        if search('UNIQUE constraint failed', str(e)):
            return return_value, 409

        return return_value, 500
    except:
        return get_exception_return(), 500

    return {}, 200


@enderecos_blueprint.route(root_path + '/<id>', methods=['GET', 'PUT', 'DELETE'])
def process_id(id):
    if request.method == 'GET':
        return show(Endereco, id)
    elif request.method == 'PUT':
        return update_local(id, request)
    elif request.method == 'DELETE':
        return delete(Endereco, id)


def update_local(id, request):
    data = request.get_json(force=True)
    not_found = []
    check_entity_presence(Cidade, not_found, cidade_field, data)
    check_entity_presence(Estado, not_found, estado_field, data)
    check_entity_presence(Pais, not_found, pais_field, data)
    if not_found:
        return {'message': 'Following fields not found: ' + ', '.join(not_found)}, 404

    return update(Endereco, id, request)