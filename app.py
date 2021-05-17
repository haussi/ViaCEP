
from flask import Flask, render_template, request, url_for
import requests


app = Flask(__name__)

cep = ""
resultado_get = ""

@app.route("/")
def index():
    return render_template("index.html")



@app.route("/", methods=['GET', 'POST'])
def busca_cep():
    cep = request.form['cep']

    resultado_get = requests.get("https://viacep.com.br/ws/" + cep + "/json/").json()

    return render_template("resultado.html", resultado_get=resultado_get)

app.run(debug=True)