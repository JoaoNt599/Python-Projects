from flask import Blueprint
from flaskr.service import pessoa_service

pessoas_blueprint = Blueprint('pessoas', __name__, url_prefix='/pessoas')


@pessoas_blueprint.route('/cpf/<string:cpf>', methods=['GET'])
def obter_pessoa_pelo_cpf(cpf):
    return pessoa_service.obter_pessoa_pelo_cpf(cpf)