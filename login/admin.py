from db import db
from models import User


usuarios = db.session.query(User).filter_by(id= 3).first()
db.session.delete(usuarios)
db.session.commit()
print("Usuario deletado com sucesso!")

