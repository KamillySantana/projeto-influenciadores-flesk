from flask import Flask, render_template, request, redirect

app = Flask(__name__)

class Influencers:
    def __init__(self, nome, plataformas, seguidores, interesses):
        self.nome = nome
        self.plataformas = plataformas
        self.seguidores = seguidores
        self.interesses = interesses

listaIn = []

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/influencers')
def influencers():
    return render_template('influenciadores.html', Titulo = "Influenciadores", listaIn = listaIn)

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html', Titulo = "Cadastre-se")


@app.route('/rotaInter', methods=['POST'])
def rotaInter():
    nome = request.form['nome']
    plataformas = request.form['plataformas']
    seguidores = request.form['seguidores']
    interesses = request.form['interesses']
    objIn = Influencers(nome,plataformas,seguidores,interesses)
    listaIn.append(objIn)
    return redirect('/influencers')

if __name__ == '__main__':
    app.run()
