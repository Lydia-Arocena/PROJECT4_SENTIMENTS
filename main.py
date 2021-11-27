from flask import Flask, request
from flask import jsonify
import config.tools as sqt

app = Flask(__name__)

@app.route("/autores")
def listado_autores():
    authors = sqt.get_autores()
    return jsonify(authors)
  




app.run(debug=True)