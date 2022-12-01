from flask import Blueprint, render_template, request, redirect, url_for, session
import requests
from funcoes import Funcoes
from functools import wraps

bp_login = Blueprint('login', __name__, url_prefix='/', template_folder='templates')

urlApiFuncionarios = "http://localhost:8000/funcionario/login/"
headers = {'x-token': 'abcBolinhasToken', 'x-key': 'abcBolinhasKey'}

@bp_login.route("/", methods=['GET', 'POST'])
def login():
    return render_template("formLogin.html")

@bp_login.route('/login_usuario/', methods=['POST'])
def validaLogin():
    try:
        # dados enviados via FORM
        matricula = request.form['matricula']
        senha = Funcoes.cifraSenha(request.form['senha'])
        # monta o JSON para envio a API
        payload = {'id_funcionario': 0, 'nome': '', 'matricula': matricula, 'cpf': '', 'telefone': '', 'grupo': 0, 'senha': senha, 'status': 1}
        # executa o verbo POST da API e armazena seu retorno
        response = requests.post(urlApiFuncionarios, headers=headers, json=payload)
        result = response.json()

        if (response.status_code != 200 or result[1] != 200):
            raise Exception(result[0])

        # limpa a sessão atual e registra usuário na sessão, armazenando o login do usuário
        session.clear()
        session['nome'] = result[0]['nome']
        session['login'] = result[0]['cpf']
        session['grupo'] = result[0]['grupo']
        # abre a aplicação na tela home
        
        return result
    except Exception as e:
        # retorna para a tela de login
        
        return e

@bp_login.route("/logoff", methods=['GET'])
def logoff():
    # limpa um valor individual
    session.pop('login', None)

    # limpa toda sessão
    session.clear()

    # retorna para a tela de login
    return redirect(url_for('login.login'))

# valida se o usuário esta ativo na sessão
def validaSessao(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'login' not in session:
            # descarta os dados copiados da função original e retorna a tela de login
            return redirect(url_for('login.login'))
        else:
            # retorna os dados copiados da função original
            return f(*args, **kwargs)
    # retorna o resultado do if acima
    return decorated_function