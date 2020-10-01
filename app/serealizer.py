from flask_marshmallow import Marshmallow

from .model import Clientes, Pedidos, Produtos

ma = Marshmallow()


def configure(app):
    ma.init_app(app)


class ClientesSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Clientes
        load_instance = True


class PedidosSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Pedidos
        load_instance = True


class ProdutosSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Produtos
        load_instance = True
