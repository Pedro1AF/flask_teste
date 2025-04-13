from flask import Flask, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config['SECRET_KEY'] = 'secretkeysql'
db = SQLAlchemy(app)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)

@app.route('/criar_conta')
def criar_conta():
    return render_template('acesse_conta.html')

@app.route('/terms_client')
def termos_cliente():
    return render_template('termos_user.html')

@app.route('/entrar_conta')
def entrar_conta():
    return render_template('criar_conta.html')

if __name__ == '__main__':
    app.run(debug=True)
