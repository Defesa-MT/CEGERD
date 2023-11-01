from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    nome = request.form.get('nome')
    senha = request.form.get('senha')

    if nome == 'defesa' and senha == '123':
        return redirect('/dados')
    else:
        error = "Senha incorreta. Tente novamente."
        return render_template('login.html', error=error)

@app.route('/dados')
def dados():
    return render_template('dados.html')


@app.route('/mapa')
def mapa():
    return render_template('mapa.html')
  
  
if __name__ == "__main__":
    app.run(debug=True)

# servidor do heroku

