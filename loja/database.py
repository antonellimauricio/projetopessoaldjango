from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # Usando SQLite, você pode mudar para outro banco de dados se preferir
db = SQLAlchemy(app)

class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    cidade = db.Column(db.String(100), nullable=False)
    cep = db.Column(db.String(10), nullable=False)
    subsetor_nome = db.Column(db.String(50), nullable=False)

class ClienteRepository:
    def cadastrar_cliente(self, cliente):
        db.session.add(cliente)
        db.session.commit()

    def listar_clientes(self, subsetor_nome):
        return Cliente.query.filter_by(subsetor_nome=subsetor_nome).all()

cliente_repo = ClienteRepository()

class Setor:
    def __init__(self, nome, subsetores=[]):
        self.nome = nome
        self.subsetores = subsetores

class Subsetor:
    def __init__(self, nome, paginas=[]):
        self.nome = nome
        self.paginas = paginas


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
