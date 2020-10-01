# API PB
O projeto possui como objetivo disponibilizar uma API para cadastros

## Instalação
Baixe o projeto através do GitHub ou copie o comando e execute em seu console.

```sh
$ git clone https://github.com/thiagosousacosta/api_bd.git
```

## Utilização

Execute os seguintes comandos para estabelecer as variáveis de ambiente:

```sh
$ SET FLASK_APP=app
$ SET FLASK_ENV=Development
$ SET FLASK_DEBUG=True
```

e execute:

```sh
$ flask db init
$ flask db migrate
$ flask db upgrade
```

Para configurar o banco.

Agora basta executar o seguinte comando para rodar a aplicação:

```sh
$ flask run
```

Os endpoint disponpiveis são:

1.  Clientes
    - /clientes/mostrar
    - /clientes/deletar/{id}
    - /clientes/modificar/{id}
    - /clientes/cadastrar

2. Produtos
    - /produtos/mostrar
    - /produtos/deletar/{id}
    - /produtos/modificar/{id}
    - /produtos/cadastrar

3. Pedidos
    - /pedidos/mostrar
    - /pedidos/deletar/{id}
    - /pedidos/modificar/{id}
    - /pedidos/cadastrar