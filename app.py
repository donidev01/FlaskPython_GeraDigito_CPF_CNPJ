
from flask import Flask, flash, render_template

from src import geradorDigito, geradorDocumento

app = Flask(__name__)

# configuração da rotas.

# index
@app.route("/")
def index():
    return render_template("index.html")

@app.route('/geradorDigito')
def geradorDig():
    return render_template('geradorDigito.html')

@app.route('/geradorDigito', methods=['POST'])
def geradorDig1():
    docs = geradorDigito.get_tp_pess()
    return render_template('geradorDigito.html', docs=docs)

@app.route('/geradorDocumento')
def geradorDoc():
    return render_template('geradorDocumento.html')

@app.route('/geradorDocumento', methods=['POST'])
def geradorDoc1():
    docs = geradorDocumento.get_tp_pess()
    return render_template('geradorDocumento.html', docs=docs)


app.run(debug=True)
