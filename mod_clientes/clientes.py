from flask import Blueprint, render_template, request, jsonify
from mod_login.login import validaSessao
import requests
from funcoes import Funcoes

bp_cliente = Blueprint('cliente', __name__, url_prefix="/cliente", template_folder='templates')

''' endereços do endpoint '''
urlApiClientes = "http://localhost:8000/cliente/"
headers = {'x-token': 'abcBolinhasToken', 'x-key': 'abcBolinhasKey'}

''' rotas dos formulários '''
@bp_cliente.route('/', methods=['GET', 'POST'])
@validaSessao
def ListaCliente():
    try:
        response = requests.get(urlApiClientes, headers=headers)
        result = response.json()
        if(response.status_code != 200):
            raise Exception(result)
        return render_template('ListaClientes.html', result = result), 200
    except Exception as e:
        return render_template('ListaClientes.html', erro=e)


@bp_cliente.route('/salvar_cliente/', methods=['POST'])
def insert():
    try:
        # dados enviados via FORM
        id = request.form['id']
        nome = request.form['nome']
        matricula = request.form['login']
        login = request.form['login']
        documento = request.form['documento']
        telefone = request.form['telefone']
        grupo = request.form['grupo']
        senha = Funcoes.cifraSenha(request.form['senha'])
        # monta o JSON para envio a API
        payload = {'id': id, 'nome': nome, 'matricula': matricula,'cpf': documento, 'telefone': telefone, 'pega_fiado': grupo, 'login':login, 'senha': senha, 'status': 1}
        # executa o verbo POST da API e armazena seu retorno
        response = requests.post(urlApiClientes, headers=headers, json=payload)
        result = response.json()
        return result
    except Exception as e:
        return e

@bp_cliente.route('/editar_cliente/', methods=['POST'])
def update():
    try:
        # dados enviados via FORM
        
        id = request.form['id']
        nome = request.form['nome']
        matricula = request.form['login']
        login = request.form['login']
        documento = request.form['documento']
        telefone = request.form['telefone']
        grupo = request.form['grupo']
        senha = Funcoes.cifraSenha(request.form['senha'])
        # monta o JSON para envio a API
        payload = {'id': id, 'nome': nome, 'matricula': matricula,'cpf': documento, 'telefone': telefone, 'pega_fiado': grupo, 'login':login, 'senha': senha, 'status': 1}
        # executa o verbo POST da API e armazena seu retorno
        response = requests.put(urlApiClientes + id, headers=headers, json=payload)
        result = response.json()
        return result
    except Exception as e:
        return e

@bp_cliente.route("/form-edit-cliente", methods=['POST'])
@validaSessao
def formEditCliente():
    try:
        # ID enviado via FORM
        id_funcionario = request.form['id']
        # executa o verbo GET da API buscando somente o funcionário selecionado,
        # obtendo o JSON do retorno
        response = requests.get(urlApiClientes + id_funcionario, headers=headers)
        result = response.json()
        if (response.status_code != 200 or result[1] != 200):
            raise Exception(result[0])
        # renderiza o form passando os dados retornados
        return render_template('formListaClientes.html', result=result[0])
    except Exception as e:
        return render_template('ListaClientes.html', msgErro=e.args[0])
@bp_cliente.route('/deletar_prod/', methods=['POST'])
def delete():
    try:
        # dados enviados via FORM
        id = request.form['id']
        # executa o verbo DELETE da API e armazena seu retorno
        response = requests.delete(
        urlApiClientes + id, headers=headers)
        result = response.json()
        if (response.status_code != 200 or result[1] != 201):
            raise Exception(result[0])
        return jsonify(erro=False, msg=result[0])
    except Exception as e:
        return jsonify(erro=True, msgErro=e.args[0])

''' rotas dos formulários '''
@bp_cliente.route('/cadastrar/', methods=['GET'])
@validaSessao
def formListaCliente():
    return render_template('formListaClientes.html'), 200