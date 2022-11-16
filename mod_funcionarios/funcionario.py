from flask import Blueprint, render_template, request 
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
        matricula = request.form['matricula']
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

'''
Rota antiga de app...
@app.route('/funcionario/')
def formListaFuncionario():
# return "<h1>Rota da página de Funcionários da nossa WEB APP</h1>", 200
return render_template('formListaFuncionario.html'), 200
'''