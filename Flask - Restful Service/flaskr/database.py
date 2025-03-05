from flask_sqlalchemy import SQLAlchemy
from flask_seeder import FlaskSeeder

db = SQLAlchemy()
Base = db.Model


def init_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://webservice.db'
    app.config['SQLALCHEMY_ECHO'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    seeder = FlaskSeeder()
    seeder.init_app(app, db)

    import flaskr.model.pais
    import flaskr.model.estado
    import flaskr.model.cidade
    import flaskr.model.endereco
    import flaskr.model.pessoa

    db.create_all(app=app)
