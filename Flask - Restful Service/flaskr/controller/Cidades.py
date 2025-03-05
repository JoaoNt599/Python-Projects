from flask import Blueprint, request
from flaskr.database import db_session
from flaskr.models import Cidade

from flaskr.controller.RestCommon import index, create, show, update, delete

cidades_blueprint = Blueprint('cidades', __name__)
root_path = '/cidades'


@cidades_blueprint.route(root_path, methods=['GET', 'POST'])
def process_root():
    if request.method == 'GET':
        return index(Cidade)
    else:
        return create(Cidade, request)


@cidades_blueprint.route(root_path + '/<id>', methods=['GET', 'PUT', 'DELETE'])
def process_id(id):
    if request.method == 'GET':
        return show(Cidade, id)
    elif request.method == 'PUT':
        return update(Cidade, id, request)
    elif request.method == 'DELETE':
        return delete(Cidade, id)
