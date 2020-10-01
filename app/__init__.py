import os

from flask import Flask
from flask_migrate import Migrate

from .model import configure as config_db
from .serealizer import configure as config_ma


def create_app():
    app = Flask(__name__)
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'teste_bp.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    config_db(app)
    config_ma(app)

    Migrate(app, app.db)

    from .clientes import bp_clientes
    from .pedidos import bp_pedidos
    from .produtos import bp_produtos

    app.register_blueprint(bp_clientes)
    app.register_blueprint(bp_pedidos)
    app.register_blueprint(bp_produtos)

    return app
