from config.configuration import engine
import pandas as pd
from main import listado_frases
from textblob import TextBlob
from googletrans import Translator



def get_autores():
    query = list(engine.execute("SELECT distinct(Nombre) FROM proyecto_sentiments2.author;"))
    lista =  [{"nombre": elemento[0]} for elemento in query]
    return lista


def get_quotes():
    query= list(engine.execute("SELECT (Frases) FROM proyecto_sentiments2.quotes;"))
    lista_frases =  [{"frase": elemento[0]} for elemento in query]
    return lista_frases



def translation(lang):
    trans = Translator()
    if lang == "en":
        return listado_frases()
    elif lang == "es":
        frase = listado_frases()
        traducida= trans.translate(frase(), dest="es").text
        return f"{traducida}"
    else:
        return listado_frases()
