from config.configuration import engine
import pandas as pd
from textblob import TextBlob




def get_autores():
    query = list(engine.execute("SELECT distinct(Nombre) FROM proyecto_sentiments2.author;"))
    lista =  [{"nombre": elemento[0]} for elemento in query]
    return lista


def get_quotes():
    query= list(engine.execute("SELECT (Frases) FROM proyecto_sentiments2.quotes;"))
    lista_frases =  [{"frase": elemento[0]} for elemento in query]
    return lista_frases

