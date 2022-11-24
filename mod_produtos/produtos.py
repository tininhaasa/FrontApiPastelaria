from flask import Blueprint, render_template, request, jsonify
import requests
import base64

bp_produto = Blueprint('produto', __name__, url_prefix="/produto", template_folder='templates')

''' endereços do endpoint '''
urlApiProdutos = "http://localhost:8000/produto/"
headers = {'x-token': 'abcBolinhasToken', 'x-key': 'abcBolinhasKey'}

''' rotas dos formulários '''
@bp_produto.route('/cadastrar/', methods=['GET'])
def formListaProduto():
    return render_template('formListaProdutos.html'), 200

@bp_produto.route('/salvar_produto/', methods=['POST'])
def insert():
    try:
        # dados enviados via FORM
        id = request.form['id']
        nome = request.form['name']
        descricao = request.form['desc']
        qtd = request.form['qtd']
        valor_unitario = request.form['price']
        # converte a foto em base64
        foto = "data:" + request.files['image_product'].content_type + ";base64," + str(base64.b64encode(request.files['image_product'].read()), "utf-8")
        # foto = ""
        # monta o JSON para envio a API
        payload = {'id': id, 'nome': nome, 'descricao': descricao, 'qtd': qtd, 'foto': foto, 'preco': valor_unitario, 'status': 1}
        # executa o verbo POST da API e armazena seu retorno
        response = requests.post(urlApiProdutos, headers=headers, json=payload)
        result = response.json()
        return result
    except Exception as e:
        return e

@bp_produto.route('/editar_produto/', methods=['POST'])
def update():
    try:
        # dados enviados via FORM
        id = request.form['id']
        nome = request.form['name']
        descricao = request.form['desc']
        qtd = request.form['qtd']
        valor_unitario = request.form['price']
        # converte a foto em base64
        foto = "data:" + request.files['image_product'].content_type + ";base64," + str(base64.b64encode(request.files['image_product'].read()), "utf-8")
        # foto = ""
        # monta o JSON para envio a API
        payload = {'id': id, 'nome': nome, 'descricao': descricao, 'qtd': qtd, 'foto': foto, 'preco': valor_unitario, 'status': 1}
        # executa o verbo POST da API e armazena seu retorno
        response = requests.put(urlApiProdutos+ id, headers=headers, json=payload)
        result = response.json()
        return result
    except Exception as e:
        return e

@bp_produto.route('/deletar_prod/', methods=['POST'])
def delete():
    try:
        # dados enviados via FORM
        id_produto = request.form['id']
        # executa o verbo DELETE da API e armazena seu retorno
        response = requests.delete(
        urlApiProdutos + id_produto, headers=headers)
        result = response.json()
        if (response.status_code != 200 or result[1] != 201):
            raise Exception(result[0])
        return jsonify(erro=False, msg=result[0])
    except Exception as e:
        return jsonify(erro=True, msgErro=e.args[0])

''' rotas dos formulários '''
@bp_produto.route('/', methods=['GET', 'POST'])
def ListaProdutos():
    try:
        response = requests.get(urlApiProdutos, headers=headers)
        result = response.json()
       
        if(response.status_code != 200):
            raise Exception(result)
        return render_template('ListaProdutos.html', result = result), 200
    except Exception as e:
        return render_template('ListaProdutos.html', erro=e)

@bp_produto.route("/form-edit-produto", methods=['POST'])
def formEditProduto():
    try:
        # ID enviado via FORM
        id_funcionario = request.form['id']
        # executa o verbo GET da API buscando somente o funcionário selecionado,
        # obtendo o JSON do retorno
        response = requests.get(urlApiProdutos + id_funcionario, headers=headers)
        result = response.json()
        if (response.status_code != 200 or result[1] != 200):
            raise Exception(result[0])
        # renderiza o form passando os dados retornados
        return render_template('formListaProdutos.html', result=result[0])
    except Exception as e:
        return render_template('ListaProdutos.html', msgErro=e.args[0])

'''
Rota antiga de app...
@app.route('/produto/')
def formListaproduto():
# return "<h1>Rota da página de Funcionários da nossa WEB APP</h1>", 200
return render_template('formListaproduto.html'), 200
'''