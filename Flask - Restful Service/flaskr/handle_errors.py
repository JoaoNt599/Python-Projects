from flask import jsonify, make_response
from sqlalchemy.orm.exc import NoResultFound


def handle_404(exception):
    code = 404
    json = jsonify({
        "code": code,
        "error": "O recurso solicitado não foi encontrado."
    })
    response = make_response(json, code)
    response.headers['Content-Type'] = 'application/json'
    return response


def handle_noresultfound_exception(exception):
    if isinstance(exception, NoResultFound):
        code = 404
        json = jsonify({
            "code": code,
            "error": "Nenhum resultado foi encontrado."
        })
        response = make_response(json, code)
        response.headers['Content-Type'] = 'application/json'
        return response
