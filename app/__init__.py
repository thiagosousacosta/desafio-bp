import os

from flask import Flask


def create_app():
    app = Flask(__name__)
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'teste_bp.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    return app
