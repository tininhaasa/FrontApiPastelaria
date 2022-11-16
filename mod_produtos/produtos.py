from flask import Blueprint, render_template, request
import requests
import base64
bp_produto = Blueprint('produto', __name__, url_prefix="/produto", template_folder='templates')

''' endereços do endpoint '''
urlApiProdutos = "http://localhost:8000/produto/"
urlApiProduto = "http://localhost:8000/produto/%s"
headers = {'x-token': 'abcBolinhasToken', 'x-key': 'abcBolinhasKey'}

''' rotas dos formulários '''
@bp_produto.route('/cadastrar/', methods=['GET'])
def formListaProduto():
    return render_template('formListaProdutos.html'), 200

@bp_produto.route('/insert/', methods=['POST'])
def insert():
    try:
        # dados enviados via FORM
        id = request.form['id']
        nome = request.form['name']
        descricao = request.form['desc']
        qtd = request.form['qtd']
        #foto = request.form['foto']
        valor_unitario = request.form['price']
        # converte a foto em base64
        foto = "data:" + request.files['image_product'].content_type + ";base64," + str(base64.b64encode(request.files['image_product'].read()), "utf-8")

        # monta o JSON para envio a API
        payload = {'id': id, 'nome': nome, 'descricao': descricao, 'qtd': qtd, 'foto': foto, 'valor_unitario': valor_unitario}
        # executa o verbo POST da API e armazena seu retorno
        response = requests.post(urlApiProdutos, headers=headers, json=payload)
        result = response.json()
        return render_template('formListaProduto.html', msg=result)
    except Exception as e:
        return render_template('formListaProduto.html', msgErro=e)

''' rotas dos formulários '''
@bp_produto.route('/', methods=['GET', 'POST'])
def ListaProdutos():
    try:
        response = requests.get(urlApiFuncionarios, headers=headers)
        result = response.json()
        if(response.status_code != 200):
            raise Exception(result)
        return render_template('ListaProdutos.html', result = result), 200
    except Exception as e:
        return render_template('ListaProdutos.html', erro=e)

'''
Rota antiga de app...
@app.route('/produto/')
def formListaproduto():
# return "<h1>Rota da página de Funcionários da nossa WEB APP</h1>", 200
return render_template('formListaproduto.html'), 200
'''