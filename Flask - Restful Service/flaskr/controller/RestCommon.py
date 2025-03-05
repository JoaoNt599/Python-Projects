from flaskr.controller.Utils import get_exception_return
from flask import jsonify
from flaskr.database import db_session
from sqlalchemy import exc
import sys


def index(model):
    query_result = model.query.all()
    entities = [];
    for entity in query_result:
        entities.append(entity.to_dict())

    return jsonify(entities)


def create(model, request):
    data = request.get_json(force=True)

    try:
        nome = data['nome']
        sigla = data['sigla']
    except:
        return {'message': 'Fields id, nome, and sigla are required'}, 400

    try:
        new_entity = model(nome=nome, sigla=sigla)
        db_session.add(new_entity)
        db_session.commit()
    except exc.IntegrityError:
        return_value = get_exception_return()
        if search('UNIQUE constraint failed', str(e)):
            return return_value, 409

        return return_value, 500
    except:
        return get_exception_return(), 500

    return {}, 200


def show(model, id):
    entity = model.query.filter_by(id=id).first()
    if entity:
        return jsonify(entity.to_dict())
    else:
        return {}, 404


def update(model, id, request):
    if model.query.filter_by(id=id).first():
        data = request.get_json(force=True)
        update_query = {}
        for key in data:
            update_query[key] = data[key]

        if 'id' in update_query:
            return {'message': 'Can not change Id'}, 400

        try:
            db_session.query(model).filter_by(id=id).update(update_query)
            db_session.commit()
        except:
            return get_exception_return(), 500

        return {}, 200
    else:
        return {}, 404


def delete(model, id):
    try:
        entity = model.query.filter_by(id=id).first()
        if entity is None:
            return {}, 404

        db_session.delete(entity)
        db_session.commit()

        return {}, 200
    except:
        return get_exception_return(), 500
