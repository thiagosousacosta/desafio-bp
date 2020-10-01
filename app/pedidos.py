from flask import Blueprint, current_app, jsonify, request

from .model import Pedidos
from .serealizer import PedidosSchema

bp_pedidos = Blueprint('pedidos', __name__)


@bp_pedidos.route('/pedidos/mostrar', methods=['GET'])
def mostrar():
    try:
        peds = PedidosSchema(many=True)
        result = Pedidos.query.all()
        return peds.jsonify(result), 200
    except:
        return jsonify('Erro ao processar'), 400
    

@bp_pedidos.route('/pedidos/deletar/<id>', methods=['DELETE'])
def deletar(id):
    try:
        Pedidos.query.filter(Pedidos.id == id).delete()
        current_app.db.session.commit()
        return jsonify('Deletado'), 200
    except:
        return jsonify('Erro ao processar'), 400


@bp_pedidos.route('/pedidos/modificar/<id>', methods=['PUT'])
def modificar(id):
    try:
        peds = PedidosSchema()
        query = Pedidos.query.filter(Pedidos.id == id)
        query.update(request.json)
        current_app.db.session.commit()
        return peds.jsonify(query.first()), 200
    except:
        return jsonify('Erro ao processar'), 400
    

@bp_pedidos.route('/pedidos/cadastrar', methods=['POST'])
def cadastrar():
    try:
        peds = PedidosSchema()
        pedido = peds.load(request.json)
        current_app.db.session.add(pedido)
        current_app.db.session.commit()
        return peds.jsonify(pedido), 201
    except:
        return jsonify('Erro ao processar'), 400
