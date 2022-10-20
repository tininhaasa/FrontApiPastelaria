from flask import Blueprint, render_template
bp_cliente = Blueprint('comandas', __name__, url_prefix="/comandas", template_folder='templates')

''' rotas dos formulários '''
@bp_cliente.route('/')
def formListaCliente():
    return render_template('formListaClientes.html'), 200

'''
Rota antiga de app...
@app.route('/cliente/')
def formListacliente():
# return "<h1>Rota da página de Funcionários da nossa WEB APP</h1>", 200
return render_template('formListacliente.html'), 200
'''