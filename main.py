from flask import Flask, request
from flask import jsonify
import src.tools as sqt
import src.NLP_functions as sent

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


@app.route("/frases_/<genero>/<autor>") 
def random_aut_gen(genero, autor):
    ran = sqt.random_aut_gen(genero, autor)
    return jsonify(ran)


@app.route("/frases_lan/<genero>/<autor>") 
def random_aut_gen_idioma(genero, autor):
    lan = request.args.get("idioma")
    ran = sqt.random_aut_gen_2(lan, genero, autor)
    return jsonify(ran)



@app.route("/NLP/<autor>") 
def sentimientos(autor):
    df=sent.NLP_createdf(autor)
    df["tokenizadas"]=df.Frases.apply(sent.NLP_tokenizer)
    df["compound"]= df.tokenizadas.apply(sent.NLP_sentiment)
    print(df)
    return str(df.compound.mean())



@app.route("/nuevafrase", methods=["POST"])
def insertafrase():
    author = request.form.get("author")
    genre = request.form.get("genre")
    quote = request.form.get("quote")
    return sqt.nuevafrase(author, genre, quote)


@app.route("/nuevoautor", methods=["POST"])
def insertaautor():
    author = request.form.get("author")
    return sqt.nuevoautor(author)





app.run(debug=True)