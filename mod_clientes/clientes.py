from flask import Blueprint, render_template


bp_cliente = Blueprint('cliente', __name__, url_prefix="/cliente", template_folder='templates')

''' rotas dos formulários '''
@bp_cliente.route('/')
def ListaCliente():
    return render_template('ListaClientes.html'), 200

cd_cliente = Blueprint('cadastrarcliente', __name__, url_prefix="/cadastrar-cliente", template_folder='templates')

''' rotas dos formulários '''
@cd_cliente.route('/')
def formListaCliente():
    return render_template('formListaClientes.html'), 200