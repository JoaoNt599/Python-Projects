from flask import Flask
from flaskr.database import init_db
from sqlalchemy.orm.exc import NoResultFound


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    init_db(app)

    from flaskr.controller.pessoa_controller import pessoas_blueprint
    from flaskr.controller.home_controller import home_blueprint
    app.register_blueprint(pessoas_blueprint)
    app.register_blueprint(home_blueprint)

    from flaskr import handle_errors
    app.register_error_handler(NoResultFound, handle_errors.handle_noresultfound_exception)
    app.register_error_handler(404, handle_errors.handle_404)

    return

