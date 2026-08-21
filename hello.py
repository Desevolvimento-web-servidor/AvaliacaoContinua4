from datetime import datetime
from flask import Flask, request, redirect,abort, render_template, session, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, PasswordField
from wtforms.validators import DataRequired
from flask_moment import Moment
from flask_bootstrap import Bootstrap

app = Flask(__name__, static_folder='templates/static')
moment=Moment(app)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY']='Chave Forte'

class CadastroForm(FlaskForm):
    name = StringField('Informe o seu nome', validators=[DataRequired()])
    sobrenome = StringField('Informe o seu sobrenome', validators=[DataRequired()])
    instituicao = StringField('Informe a sua instituição de ensino', validators=[DataRequired()])
    disciplina = SelectField('Informe a sua disciplina', choices=[('DSWA5', 'DSWA5'), ('DSWA4', 'DSWA4'), ('Gestão de projetos', 'Gestão de projetos')], validators=[DataRequired()])
    submit = SubmitField('Submit')
class LoginForm(FlaskForm):
    nome = StringField('Nome ou e-mail', validators=[DataRequired()])
    senha = PasswordField('Informe a sua senha', validators=[DataRequired()])
    enviar = SubmitField('Enviar')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = CadastroForm()

    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Você alterou o seu nome!')

        session['name'] = form.name.data
        session['sobrenome'] = form.sobrenome.data
        session['instituicao'] = form.instituicao.data
        session['disciplina'] = form.disciplina.data
        session['ip_computador'] = request.remote_addr
        session['host_atual'] = request.host

        return redirect(url_for('index'))

    return render_template(
        'home.html',
        current_time=datetime.utcnow(),
        form=form,
        # Puxa direto da session (se não houver, fica None)
        ip_computador=session.get('ip_computador'),
        host_atual=session.get('host_atual'),
        name=session.get('name'),
        sobrenome=session.get('sobrenome'),
        instituicao=session.get('instituicao'),
        disciplina=session.get('disciplina')
    )

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        session['nome']=form.nome.data
        return redirect(url_for('sucesso'))
    return render_template('login.html', current_time=datetime.utcnow(), form=form)
@app.route('/sucesso')
def sucesso():
    nome=session.get('nome')
    return render_template('sucesso.html', nome=nome, current_time=datetime.utcnow())
@app.route('/identificacao/<nome>/<protuario>/<instituicao>')
def identificacao(nome, protuario, instituicao):
    return render_template("identificacao.html", nome=nome, protuario=protuario, instituicao=instituicao)


@app.route('/abortar')
def abortar():
    abort(404)