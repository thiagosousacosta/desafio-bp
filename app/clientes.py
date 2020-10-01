from flask import Blueprint, current_app, jsonify, request

from .model import Clientes
from .serealizer import ClientesSchema

bp_clientes = Blueprint('clientes', __name__)


@bp_clientes.route('/clientes/mostrar', methods=['GET'])
def mostrar():
    try:
        clis = ClientesSchema(many=True)
        result = Clientes.query.all()
        return clis.jsonify(result), 200
    except:
        return jsonify('Erro ao processar'), 400
    

@bp_clientes.route('/clientes/deletar/<id>', methods=['DELETE'])
def deletar(id):
    try:
        Clientes.query.filter(Clientes.id == id).delete()
        current_app.db.session.commit()
        return jsonify('Deletado')
    except:
        return jsonify('Erro ao processar'), 400


@bp_clientes.route('/clientes/modificar/<id>', methods=['PUT'])
def modificar(id):
    try:
        clis = ClientesSchema()
        query = Clientes.query.filter(Clientes.id == id)
        query.update(request.json)
        current_app.db.session.commit()
        return clis.jsonify(query.first())
    except:
        return jsonify('Erro ao processar'), 400
    

@bp_clientes.route('/clientes/cadastrar', methods=['POST'])
def cadastrar():
    try:
        clis = ClientesSchema()
        cliente = clis.load(request.json)
        current_app.db.session.add(cliente)
        current_app.db.session.commit()
        return clis.jsonify(cliente), 201
    except:
        return jsonify('Erro ao processar'), 400
