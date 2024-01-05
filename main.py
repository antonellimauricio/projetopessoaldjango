from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

class Cliente:
    def __init__(self, nome, idade, email, cidade, cep):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.cidade = cidade
        self.cep = cep

class ClienteRepository:
    clientes = []

    def cadastrar_cliente(self, cliente):
        self.clientes.append(cliente)

    def listar_clientes(self):
        return self.clientes

cliente_repo = ClienteRepository()

class Setor:
    def __init__(self, nome, subsetores=[]):
        self.nome = nome
        self.subsetores = subsetores

class Subsetor:
    def __init__(self, nome, paginas=[]):
        self.nome = nome
        self.paginas = paginas

# Criar setores e subsetores
home = Setor("Home")
masculino = Setor("Masculino", [Subsetor("Beleza"), Subsetor("Calçados Masculinos")])
feminino = Setor("Feminino", [Subsetor("Beleza"), Subsetor("Calçados Femininos")])
esportes = Setor("Esportes", [Subsetor("Esporte")])

@app.route('/')
def index():
    return render_template('index.html', setores=[home, masculino, feminino, esportes])

@app.route('/subsetor/<subsetor_nome>')
def subsetor(subsetor_nome):
    return render_template('subsetor.html', subsetor_nome=subsetor_nome)

@app.route('/subsetor/<subsetor_nome>/cadastrar_cliente', methods=['GET', 'POST'])
def cadastrar_cliente(subsetor_nome):
    if request.method == 'POST':
        nome = request.form['nome']
        idade = request.form['idade']
        email = request.form['email']
        cidade = request.form['cidade']
        cep = request.form['cep']

        novo_cliente = Cliente(nome, idade, email, cidade, cep)
        cliente_repo.cadastrar_cliente(novo_cliente)

        return redirect(url_for('subsetor', subsetor_nome=subsetor_nome))

    return render_template('cadastrar_cliente.html', subsetor_nome=subsetor_nome)

if __name__ == '__main__':
    app.run(debug=True)
