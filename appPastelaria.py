from flask import Flask,render_template
from mod_funcionarios.funcionario import bp_funcionario
from mod_clientes.clientes import bp_cliente
from mod_produtos.produtos import bp_produto
from mod_index.index import bp_index
from mod_funcionarios.funcionario import cd_funcionario
from mod_clientes.clientes import cd_cliente
from mod_produtos.produtos import cd_produto
from mod_erro.erro import bp_erro

app = Flask(__name__)

''' chamadas dos formulários '''

# registro das rotas do blueprint
app.register_blueprint(bp_funcionario)
app.register_blueprint(bp_cliente)
app.register_blueprint(bp_produto)
app.register_blueprint(bp_index)
app.register_blueprint(cd_funcionario)
app.register_blueprint(cd_cliente)
app.register_blueprint(cd_produto)
app.register_blueprint(bp_erro)

if __name__ == "__main__":
    """ Inicia o aplicativo WEB Flask """
    app.run(host='0.0.0.0', port=5000, debug=True)