#pasta static, serve para armezanar imgs, css e java script
#pasta templatess, armazenar html

#metodos http sao usados para definir a ação que se deja realizar no servidor, GET, POST, PUT, DELETE
#rota intermediaria nao tem html

from flask import Flask, render_template, request, redirect

app = Flask(__name__) #criação de obj usando class Flask

class cadpokemon:
    def __init__(self, numero, nome, tipo, altura, peso):
        self.numero = numero
        self.nome = nome
        self.tipo = tipo
        self.altura = altura
        self.peso = peso

lista = []

@app.route('/pokemon')
def pokemon():
    return render_template('Pokemon.html', Titulo = "Pokémons", ListaPokemons = lista)

@app.route('/cadastro')
def cadastro():
    return render_template('Cadastro.html', Titulo = "Cadastro de Pokemon")

@app.route('/criar', methods=['POST'])
def criar():
    numero = request.form['numero']
    nome = request.form['nome']
    tipo = request.form['tipo']
    altura = request.form['altura']
    peso = request.form['peso']
    obj = cadpokemon(numero,nome,tipo,altura,peso)
    lista.append(obj)
    return redirect('/pokemon')

if __name__ == '__main__': #testa para ver c esta rodando em outro computadores
    app.run()

#=======================

#@app.route('/') #cria uma rota, / é apenas o endereço, coloca / e o que eu quero acessar
#def hello_world(): #A rota sempre espera uma função
    #return 'Hello World!'

