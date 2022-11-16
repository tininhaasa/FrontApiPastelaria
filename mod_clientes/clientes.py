from flask import Blueprint, render_template, request
import requests
from funcoes import Funcoes

bp_cliente = Blueprint('cliente', __name__, url_prefix="/cliente", template_folder='templates')

''' endereços do endpoint '''
urlApiClientes = "http://localhost:8000/cliente/"
urlApiCliente = "http://localhost:8000/cliente/%s"
headers = {'x-token': 'abcBolinhasToken', 'x-key': 'abcBolinhasKey'}

''' rotas dos formulários '''
@bp_cliente.route('/', methods=['GET', 'POST'])
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
        matricula = request.form['matricula']
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


''' rotas dos formulários '''
@bp_cliente.route('/cadastrar/', methods=['GET'])
def formListaCliente():
    return render_template('formListaClientes.html'), 200