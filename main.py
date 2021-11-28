from flask import Flask, request
from flask import jsonify
import src.tools as sqt

app = Flask(__name__)

@app.route("/autores")
def listado_autores():
    authors = sqt.get_autores()
    return jsonify(authors)
  

@app.route("/frases")
def listado_frases():
    quote = sqt.get_quotes()
    return jsonify(quote)






app.run(debug=True)