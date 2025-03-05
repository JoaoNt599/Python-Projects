from flask import Blueprint, request
from flaskr.database import db_session
from flaskr.models import Estado

from flaskr.controller.RestCommon import index, create, show, update, delete

estados_blueprint = Blueprint('estados', __name__)
root_path = '/estados'


@estados_blueprint.route(root_path, methods=['GET', 'POST'])
def process_root():
    if request.method == 'GET':
        return index(Estado)
    else:
        return create(Estado, request)


@estados_blueprint.route(root_path + '/<id>', methods=['GET', 'PUT', 'DELETE'])
def process_id(id):
    if request.method == 'GET':
        return show(Estado, id)
    elif request.method == 'PUT':
        return update(Estado, id, request)
    elif request.method == 'DELETE':
        return delete(Estado, id)
