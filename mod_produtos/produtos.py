from flask import Blueprint, render_template
cd_produto = Blueprint('cadastro_produto', __name__, url_prefix="/cadastro-produto", template_folder='templates')

''' rotas dos formulários '''
@cd_produto.route('/')
def formListaProduto():
    return render_template('formListaProdutos.html'), 200

bp_produto = Blueprint('produto', __name__, url_prefix="/produto", template_folder='templates')

''' rotas dos formulários '''
@bp_produto.route('/')
def ListaProdutos():
    return render_template('ListaProdutos.html'), 200

'''
Rota antiga de app...
@app.route('/produto/')
def formListaproduto():
# return "<h1>Rota da página de Funcionários da nossa WEB APP</h1>", 200
return render_template('formListaproduto.html'), 200
'''