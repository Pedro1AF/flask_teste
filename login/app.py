from flask import Flask, render_template, request, url_for, redirect, flash, session
import random
from flask_mail import Mail, Message
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from db import db
from models import User
import os

app = Flask(__name__)
app.secret_key = 'monedas'
lm = LoginManager(app)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'f.pedro14@escola.pr.gov.br'
app.config['MAIL_PASSWORD'] = 'pedro1411'
app.config['MAIL_DEFAULT_SENDER'] = 'monedas.verificacao@gmail.com'
app.config['MAIL_DEBUG'] = True
mail = Mail(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db.init_app(app)

class Contato:
    def __init__(self, email, senha):
        self.email = email
        self.senha = senha

def gerar_codigo_verificacao():
        return str(random.randint(10000, 99999)).zfill(5)

@lm.user_loader
def load_user(id):
    usuario_logado = db.session.query(User).filter_by(id=id).first()
    return usuario_logado

@app.route('/')
@login_required
def pagina_principal():
    load_user(current_user.nome)
    return render_template('pagina_principal.html')

@app.route('/acessar_conta', methods=['GET', 'POST'])
def acesse_conta():
    if request.method == 'GET':
        return render_template('acesse_conta.html')
    
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        usuario = db.session.query(User).filter_by(email=email).first()
        
        if usuario and usuario.password == senha:
            login_user(usuario)
            return redirect(url_for('pagina_principal'))
        else:
            flash('email ou senha incorretos.')
            return redirect(url_for('acesse_conta'))
        
@app.route('/terms_client')
def termos_cliente():
    return render_template('termos_user.html')

@app.route('/criar_conta', methods=['GET', 'POST'])
def criar_conta():
    if request.method == 'GET':
        return render_template('criar_conta.html')
    
    elif request.method == 'POST':
        nome = request.form['nome']
        cpf = request.form['cpf']
        email = request.form['email']
        telefone = request.form['telefone']
        endereco = request.form['endereco']
        senha = request.form['senha']
        novo_user = User(nome=nome, cpf=cpf, email=email, telefone=telefone, endereco=endereco, password=senha)
        db.session.add(novo_user)
        db.session.commit()
        login_user(novo_user)
    return redirect(url_for('pagina_principal'))

@app.route('/admin')
@login_required
def admin():
    if current_user.nome != 'dev.admin':
        flash('Você não tem permissão para acessar esta página.', 'error')
        return redirect(url_for('pagina_principal'))
    else:
        usuarios_lista = db.session.query(User).all()
        return render_template('admin.html', usuario_consulta=usuarios_lista)
    
@app.route('/delete/<int:id>')
def delete_user(id):
    usuario = db.session.query(User).filter_by(id=id).first()
    db.session.delete(usuario)
    db.session.commit()
    return redirect(url_for('admin'))

#@app.route('/edit/<int:id>')
#def edit_user(id):
#   editado_user = db.session.query(User).filter_by(id=id).first()
#    editado_user.nome = request.form['nome']
#   db.session.commit()
#    return redirect(url_for('admin'))
 
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)