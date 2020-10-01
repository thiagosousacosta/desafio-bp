import os

from flask import Flask
from flask_migrate import Migrate

from .model import configure as config_db


def create_app():
    app = Flask(__name__)
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'teste_bp.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    config_db(app)
 
    return app
