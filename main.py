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


@app.route("/frases/<name>") 
def autor_frase(name):
    frases = sqt.frases_porautor(name)
    return jsonify(frases)


@app.route("/frases_g/<genero>") 
def genero_frase(genero):
    generos = sqt.frase_porgenero(genero)
    return jsonify(generos)


@app.route("/random") 
def aleatoria():
    frase_dia = sqt.random_quote()
    return jsonify(frase_dia)


@app.route("/translation") 
def traduccion():
    traducida = sqt.traslation()
    return jsonify(traducida)



app.run(debug=True)