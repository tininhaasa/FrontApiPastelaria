from flask import Flask, render_template, session
from mod_funcionarios.funcionario import bp_funcionario
from mod_clientes.clientes import bp_cliente
from mod_produtos.produtos import bp_produto
from mod_index.index import bp_index
from mod_erro.erro import bp_erro
from mod_login.login import bp_login
import os

app = Flask(__name__)

''' chamadas dos formulários '''
app.secret_key = os.urandom(12).hex()
# registro das rotas do blueprint
app.register_blueprint(bp_login)
app.register_blueprint(bp_funcionario)
app.register_blueprint(bp_cliente)
app.register_blueprint(bp_produto)
app.register_blueprint(bp_index)
app.register_blueprint(bp_erro)
app.config.update(
    SESSION_COOKIE_SAMESITE='None',
    SESSION_COOKIE_SECURE='True'
)
if __name__ == "__main__":
    """ Inicia o aplicativo WEB Flask """
    app.run(host='0.0.0.0', port=5000, debug=True)