from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = 'Senai'


class Influencers:
    def __init__(self, nome, plataformas, seguidores, interesses):
        self.nome = nome
        self.plataformas = plataformas
        self.seguidores = seguidores
        self.interesses = interesses

listaIn = []

# =============================INICIO=====================================
@app.route('/inicio')
def inicio():
    if 'Usuario_Logado' not in session:
        return redirect('/')
    else:
        return render_template('inicio.html')

# =============================INICIO=====================================
@app.route('/influencers')
def influencers():
    if 'Usuario_Logado' not in session:
        return redirect('/')
    else:
        return render_template('influenciadores.html', Titulo = "Influenciadores", listaIn = listaIn)

# =============================CADASTRO=====================================
@app.route('/cadastro')
def cadastro():
    if 'Usuario_Logado' not in session:
        return redirect('/')
    else:
        return render_template('cadastro.html', Titulo = "Cadastre-se")

@app.route('/rotaInter', methods=['POST'])
def rotaInter():
    if 'salvar' in request.form:
        nome = request.form['nome']
        plataformas = request.form['plataformas']
        seguidores = request.form['seguidores']
        interesses = request.form['interesses']
        objIn = Influencers(nome,plataformas,seguidores,interesses)
        listaIn.append(objIn)
        return redirect('/influencers')
    elif 'deslogar' in request.form:
        return redirect('/')

# =============================EXCLUIR=====================================
@app.route('/excluir/<nomeinflu>', methods=['GET', 'DELETE'])
def excluir(nomeinflu):
    for i, influen in enumerate(listaIn):
        if influen.nome == nomeinflu:
            listaIn.pop(i)
            break
    return redirect('/influencers')

# =============================EDITAR=====================================
@app.route('/editar/<nomeinflu>', methods=['GET'])
def editar(nomeinflu):
    for i, influen in enumerate(listaIn):
        if influen.nome == nomeinflu:
            return render_template('Editar.html', influencier=influen, Titulo='Alterar Influenciador')

@app.route('/alterar', methods = ['POST', 'PUT'])
def alterar():
    nome = request.form['nome']
    for i, influen in enumerate(listaIn):
        if influen.nome == nome:
            influen.nome = request.form['nome']
            influen.plataformas = request.form['plataformas']
            influen.seguidores = request.form['seguidores']
            influen.interesses = request.form['interesses']
    return redirect('/influencers')

# =============================LOGIN=====================================
@app.route('/')
def login():
    session.clear()
    return render_template('Login.html', Titulo='Faça seu login')

@app.route('/autenticar', methods=['POST'])
def autenticar():
    if request.form['usuario'] == 'influ' and request.form['senha'] == '123':
        session['Usuario_Logado'] = request.form['usuario']
        flash('Usuario logado com sucesso')
        return redirect('/inicio')
    else:
        flash('Usuario não encontrado')
        return redirect('/')

if __name__ == '__main__':
    app.run()
