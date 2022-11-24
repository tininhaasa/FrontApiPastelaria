from flask import Blueprint, render_template, request , jsonify
import requests
from funcoes import Funcoes
bp_funcionario = Blueprint('funcionario', __name__, url_prefix="/funcionario", template_folder='templates')

''' endereços do endpoint '''
urlApiFuncionarios = "http://localhost:8000/funcionario/"
urlApiFuncionario = "http://localhost:8000/funcionario/%s"
headers = {'x-token': 'abcBolinhasToken', 'x-key': 'abcBolinhasKey'}

''' rotas dos formulários '''
@bp_funcionario.route('/cadastrar/', methods=['GET'])
def formListaFuncionario():
    return render_template('formListaFuncionarios.html'), 200

@bp_funcionario.route('/salvar_funcionario/', methods=['POST'])
def insert():
    try:
        # dados enviados via FORM
        id_funcionario = request.form['id']
        nome = request.form['nome']
        matricula = request.form['login']
        login = request.form['login']
        documento = request.form['documento']
        telefone = request.form['telefone']
        grupo = request.form['grupo']
        senha = Funcoes.cifraSenha(request.form['senha'])
        # monta o JSON para envio a API
        payload = {'id': id_funcionario, 'nome': nome, 'matricula': matricula,'cpf': documento, 'telefone': telefone, 'grupo': grupo, 'login':login, 'senha': senha, 'status': 1}
        # executa o verbo POST da API e armazena seu retorno
        response = requests.post(urlApiFuncionarios, headers=headers, json=payload)
        result = response.json()
        return result
    except Exception as e:
        return e

@bp_funcionario.route('/editar_funcionario/', methods=['POST'])
def update():
    try:
        # dados enviados via FORM
        id_funcionario = request.form['id']
        nome = request.form['nome']
        matricula = request.form['login']
        login = request.form['login']
        documento = request.form['documento']
        telefone = request.form['telefone']
        grupo = request.form['grupo']
        senha = Funcoes.cifraSenha(request.form['senha'])
        # monta o JSON para envio a API
        payload = {'id': id_funcionario, 'nome': nome, 'matricula': matricula,'cpf': documento, 'telefone': telefone, 'grupo': grupo, 'login':login, 'senha': senha, 'status': 1}
        # executa o verbo POST da API e armazena seu retorno
        response = requests.put(urlApiFuncionarios + id_funcionario, headers=headers, json=payload)
        result = response.json()
        return result
    except Exception as e:
        return e

@bp_funcionario.route("/form-edit-funcionario", methods=['POST'])
def formEditFuncionario():
    try:
        # ID enviado via FORM
        id_funcionario = request.form['id']
        # executa o verbo GET da API buscando somente o funcionário selecionado,
        # obtendo o JSON do retorno
        response = requests.get(urlApiFuncionarios + id_funcionario, headers=headers)
        result = response.json()
        if (response.status_code != 200 or result[1] != 200):
            raise Exception(result[0])
        # renderiza o form passando os dados retornados
        return render_template('formListaFuncionarios.html', result=result[0])
    except Exception as e:
        return render_template('ListaFuncionarios.html', msgErro=e.args[0])

''' rotas dos formulários '''
@bp_funcionario.route('/', methods=['GET', 'POST'])
def ListaFuncionarios():

    try:
        response = requests.get(urlApiFuncionarios, headers=headers)
        result = response.json()
        if(response.status_code != 200):
            raise Exception(result)
        return render_template('ListaFuncionarios.html', result = result), 200
    except Exception as e:
        return render_template('ListaFuncionarios.html', erro=e)
@bp_funcionario.route('/deletar_prod/', methods=['POST'])
def delete():
    try:
        # dados enviados via FORM
        id = request.form['id']
        # executa o verbo DELETE da API e armazena seu retorno
        response = requests.delete(
        urlApiFuncionarios + id, headers=headers)
        result = response.json()
        if (response.status_code != 200 or result[1] != 201):
            raise Exception(result[0])
        return jsonify(erro=False, msg=result[0])
    except Exception as e:
        return jsonify(erro=True, msgErro=e.args[0])

'''
Rota antiga de app...
@app.route('/funcionario/')
def formListaFuncionario():
# return "<h1>Rota da página de Funcionários da nossa WEB APP</h1>", 200
return render_template('formListaFuncionario.html'), 200
'''