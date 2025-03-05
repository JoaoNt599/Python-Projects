from flask import Blueprint, request
from flaskr.database import db_session
from flaskr.models import Pais

from flaskr.controller.RestCommon import index, create, show, update, delete

paises_blueprint = Blueprint('paises', __name__)
root_path = '/paises'


@paises_blueprint.route(root_path, methods=['GET', 'POST'])
def process_root():
    if request.method == 'GET':
        return index(Pais)
    else:
        return create(Pais, request)


@paises_blueprint.route(root_path + '/<id>', methods=['GET', 'PUT', 'DELETE'])
def process_id(id):
    if request.method == 'GET':
        return show(Pais, id)
    elif request.method == 'PUT':
        return update(Pais, id, request)
    elif request.method == 'DELETE':
        return delete(Pais, id)
