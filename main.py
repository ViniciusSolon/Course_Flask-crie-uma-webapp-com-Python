from flask import Flask, render_template

class Jogo:
    def __init__(self,nome, categoria,console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

app = Flask(__name__)



@app.route('/inicio')
def ola():
    jogo1 = Jogo('Testris','Puzzle','Atari')
    jogo2 = Jogo('God of War', 'Rack n Slash','PS2')
    jogo3 = Jogo('Mortal Kombat','luta','PS2')
    lista = [jogo1, jogo2, jogo3]
    #lista = ['Tetris', 'Skyrim', 'Crash']
    return render_template('lista.html', titulo='Jogos', jogos = lista)

app.run(host='0.0.0.0', port=8080)
