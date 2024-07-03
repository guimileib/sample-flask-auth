from database import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    # id (int), user (text), password (text) 
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True) # nullable é aceitar não ter nenhum registro dentro da coluna ou não ter | True aceita não ter nenhum registro e False não aceita
    password = db.Column(db.String(80), nullable=False) # unique é unicidade do valor no sistema | Exemplo existir apenas um User (Rodrigo)
    