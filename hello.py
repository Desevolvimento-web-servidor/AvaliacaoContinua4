from flask import Flask, request, redirect,abort, render_template, session, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_moment import Moment
from flask_bootstrap import Bootstrap

app = Flask(__name__, static_folder='templates/static')
moment=Moment(app)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY']='Chave Forte'

class NameForms(FlaskForm):
    name=StringField('What is your name?', validators=[DataRequired()])
    submit=SubmitField('Submit')
@app.route('/', methods=['GET', 'POST'])
def index():
    form=NameForms()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('home.html', form=form, name=session.get('name'))

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
