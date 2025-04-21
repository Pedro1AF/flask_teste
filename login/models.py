from db import db

class User(db.Model):
    __tablename__ = 'cadastro_usuarios'
    id = db.Column(db.Integer, primary_key=True)
    cpf = db.Column(db.String(11), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    telefone = db.Column(db.String(11), nullable=False)
    endereco = db.Column(db.String(150), nullable=False)
    nome = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
