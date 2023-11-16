#pasta static, serve para armezanar imgs, css e java script
#pasta templatess, armazenar html

from flask import Flask, render_template

app = Flask(__name__) #criação de obj usando class Flask

class cadpokemon:
    def __init__(self, numero, nome, tipo, altura, peso):
        self.numero = numero
        self.nome = nome
        self.tipo = tipo
        self.altura = altura
        self.peso = peso

@app.route('/Pokemon')
def pokemon():
    pk1 = cadpokemon(380, 'Latias', 'Dragão e psíquico', 1.4, 40)
    pk2 = cadpokemon(133,'Eevee', 'Normal',0.5,6)
    pk3 = cadpokemon(25,'Pikachu','Elétrico',0.6,4)
    lista = [pk1,pk2,pk3]

    return render_template('Pokemon.html', Titulo = "Pokémons", ListaPokemons = lista)

if __name__ == '__main__': #testa para ver c esta rodando em outro computadores
    app.run()

#=======================

#@app.route('/') #cria uma rota, / é apenas o endereço, coloca / e o que eu quero acessar
#def hello_world(): #A rota sempre espera uma função
    #return 'Hello World!'
