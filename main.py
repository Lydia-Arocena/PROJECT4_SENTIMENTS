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



@app.route("/traducido")
def translation():
    lan = request.args.get("idioma")
    frase = request.args["quote"]
    traducida = sqt.translation(lan)
    diccionario = {"frase célebre": frase, "Traducción": traducida}
    return jsonify(diccionario)





app.run(debug=True)