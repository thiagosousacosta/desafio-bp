from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

db = SQLAlchemy()

def configure(app):
    db.init_app(app)
    app.db = db

class Clientes(db.Model):
    __tablename__ = 'clientes'
    id = db.Column(db.Integer, primary_key=True)
    nome_cliente = db.Column(db.String(255))

class Produtos(db.Model):
    __tablename__ = 'produtos'
    id = db.Column(db.Integer, primary_key=True)
    descricao_produto = db.Column(db.String(255))
    valor_produto = db.Column(db.Integer)

class Pedidos(db.Model):
    __tablename__ = 'pedidos'
    id = db.Column(db.Integer, primary_key=True)
    id_cliente = db.Column(db.Integer)
    id_produto = db.Column(db.Integer)
