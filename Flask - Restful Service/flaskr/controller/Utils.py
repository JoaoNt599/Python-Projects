from os import getenv
import sys


def get_exception_return():
    if getenv('FLASK_ENV') == 'development':
        return {'message': str(sys.exc_info())}

    return {}


def check_entity_presence(model, not_found, key, data):
    if key in data:
        entity = model.query.filter_by(id=data[key]).first()
        if entity is None:
            not_found.append(key)
