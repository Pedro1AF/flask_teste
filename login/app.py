from flask import Flask, render_template, request, url_for, redirect
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from db import db
from models import User

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'your_mail_server'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'your_username'
app.config['MAIL_PASSWORD'] = 'your_password'
app.config['MAIL_DEFAULT_SENDER'] = 'your_email@example.com'
mail = Mail(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db.init_app(app)

@app.route('/', methods=['GET', 'POST'])
def acesse_conta():
     return render_template('acesse_conta.html')
        
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
        return redirect(url_for('acesse_conta'))
    else:
        return "usuarios ja cadastrados"
    
@app.route('/admin')
def admin():
    usuarios_lista = db.session.query(User).all()
    return render_template('admin.html', usuario_consulta=usuarios_lista)

@app.route('/delete/<int:id>')
def delete_user(id):
    usuario = db.session.query(User).filter_by(id=id).first()
    db.session.delete(usuario)
    db.session.commit()
    return redirect(url_for('admin'))
 
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
