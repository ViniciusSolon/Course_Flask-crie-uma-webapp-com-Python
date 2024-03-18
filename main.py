from flask import Flask, render_template, request, redirect, session, flash, url_for

class Jogo:
    def __init__(self,nome, categoria,console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

class Usuario:
    def __init__(self, nome, nickname, senha):
        self.nome = nome
        self.nickname = nickname
        self.senha = senha

usuario1 = Usuario("Vinicius Solon", "VS", "alohomora")
usuario2 = Usuario("Vinicius Solon2", "VS2", "alohomora")
usuario3 = Usuario("Vinicius Solon3", "VS3", "alohomora")

usuarios = { usuario1.nickname : usuario1,
usuario2.nickname : usuario2,
usuario3.nickname : usuario3
             }



jogo1 = Jogo('Testris','Puzzle','Atari')
jogo2 = Jogo('God of War', 'Rack n Slash','PS2')
jogo3 = Jogo('Mortal Kombat','luta','PS2')
lista = [jogo1, jogo2, jogo3]

app = Flask(__name__)
app.secret_key = 'alura'



@app.route('/')
def index():

    #lista = ['Tetris', 'Skyrim', 'Crash']
    return render_template('lista.html', titulo='Jogos', jogos = lista)

@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima = url_for('novo')))
    return render_template('novo.html', titulo ="Novo jogo")

#Pagina Intermediaria
@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome,categoria, console)
    lista.append(jogo)
    #return render_template('lista.html',titulo='jogos', jogos=lista)
    return redirect(url_for('index'))
    #url for colocamos a função que instancia nesse caso index
@app.route('/login')
def login():
    proxima = request.args.get('proxima')

    return render_template('login.html', proxima=proxima)

@app.route('/autenticar', methods=['POST',])
def autenticar():
    if request.form['usuario'] in usuarios:
        usuario = usuarios[request.form['usuario']]
        if request.form['senha'] == usuario.senha:
            session['usuario_logado'] = usuario.nickname
            flash(usuario.nickname + ' logado com sucesso!')
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)
    else:
        flash('Usuário não logado')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado  com sucesso!')
    return redirect(url_for('index'))

app.run(debug=True,host='0.0.0.0', port=8080)

"""
O Jinja2 é o motor de templates do Flask. Ele nos ajuda com diversos helpers enquanto projetamos nossos HTML de forma mais dinâmica.

Um exemplo de facilidade que temos nos templates é a ideia de filtrar um conteúdo que vem do servidor, o conteúdo de uma variável que será impressa no HTML.

Temos um trecho de código da nossa aplicação aqui:

<h1>{{  titulo  }}</h1>
COPIAR CÓDIGO
Imagine que precisamos fazer todo título de página ser iniciado com letra maiúscula no nosso template. Podemos fazer o seguinte, no trecho de código que imprime o título.

<h1>{{  titulo.upper()  }}</h1>
COPIAR CÓDIGO
Muito tranquilo de fazer esta melhoria, não é? Tem vários outros filtros que podem ajudar, como:

upper: colocar os caracteres em caixa alta;
round: arredondar números;
trim: remover espaços do início e do fim do texto;
default('texto exibido por padrão') - quando queremos mostrar algo, caso a variável esteja vazia ou nula.
Tipos de Delimitadores do Jinja2:

{%....%}: usado para inserir estruturas Python dentro de um arquivo html;
{{....}}: usado para facilitar a exibição de código python como um output em um template HTML. Alternativa: {% print(....) %};
{#....#}: usado para adicionar comentários que não serão exibidos no output do template HTML."""