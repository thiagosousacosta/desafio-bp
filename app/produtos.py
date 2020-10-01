from flask import Blueprint, current_app, jsonify, request

from .model import Produtos
from .serealizer import ProdutosSchema

bp_produtos = Blueprint('produtos', __name__)


@bp_produtos.route('/produtos/mostrar', methods=['GET'])
def mostrar():
    try:
        pros = ProdutosSchema(many=True)
        result = Produtos.query.all()
        return pros.jsonify(result), 200
    except:
        return jsonify('Erro ao processar'), 400
    

@bp_produtos.route('/produtos/deletar/<id>', methods=['DELETE'])
def deletar(id):
    try:
        Produtos.query.filter(Produtos.id == id).delete()
        current_app.db.session.commit()
        return jsonify('Deletado')
    except:
        return jsonify('Erro ao processar'), 400


@bp_produtos.route('/produtos/modificar/<id>', methods=['PUT'])
def modificar(id):
    try:
        pros = ProdutosSchema()
        query = Produtos.query.filter(Produtos.id == id)
        query.update(request.json)
        current_app.db.session.commit()
        return pros.jsonify(query.first())
    except:
        return jsonify('Erro ao processar'), 400
    

@bp_produtos.route('/produtos/cadastrar', methods=['POST'])
def cadastrar():
    try:
        pros = ProdutosSchema()
        produto = pros.load(request.json)
        current_app.db.session.add(produto)
        current_app.db.session.commit()
        return pros.jsonify(produto), 201
    except:
        return jsonify('Erro ao processar'), 400
