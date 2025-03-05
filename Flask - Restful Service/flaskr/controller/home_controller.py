from flask import Blueprint, jsonify, make_response

home_blueprint = Blueprint('home', __name__, url_prefix='/')


@home_blueprint.route('/', methods=['GET'])
def index():
    json = jsonify({
        "version": "1.0",
        "description": "API RESTful",
        "_links": {
            "pessoas": {
                "obterPessoasPeloCPF": "/pessoas/cpf/<string:cpf>"
            }
        }
    })
    response = make_response(json)
    response.headers['Content-Type'] = 'application/json'
    return response
