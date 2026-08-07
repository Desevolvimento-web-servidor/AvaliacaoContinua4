import os
from datetime import datetime, timezone, timedelta
from flask import Flask, request, redirect,abort, render_template

FUSO_BRASILIA = timezone(timedelta(hours=-3))
app = Flask(__name__, static_folder='templates/static')
@app.route('/')
def index():
    agora = datetime.now(FUSO_BRASILIA)
    data_formatada = agora.strftime('%B %d, %Y às %H:%M:%S')
    iso_date = agora.isoformat()

    return render_template("home.html", ultima_atualizacao=data_formatada, iso_date=iso_date)

@app.route('/identificacao/<nome>/<protuario>/<instituicao>')
def identificacao(nome, protuario, instituicao):
    return render_template("identificacao.html", nome=nome, protuario=protuario, instituicao=instituicao)


@app.route('/contextorequisicao/<nome>')
def contextorequisicao(nome):
    user_agent = request.headers.get('User-Agent')
    ip_computador=request.remote_addr
    host_atual=request.host
    return render_template("requisicao.html",nome=nome, user_agent=user_agent, ip_computador=ip_computador, host_atual=host_atual)

@app.route('/codigostatusdiferente')
def codigostatusdiferente():
    return '<p>Bad request</p>';

@app.route('/objetoresposta')
def objetoresposta():
    return '<h1>This document carries a cookie!</h1>'

@app.route('/redirecionamento')
def redirecionamento():
    return redirect("https://ptb.ifsp.edu.br/")

@app.route('/abortar')
def abortar():
    abort(404)
