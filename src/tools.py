from config.configuration import engine
import pandas as pd
from textblob import TextBlob
import random
from datetime import datetime
from googletrans import Translator



def get_autores():
    query = list(engine.execute("SELECT distinct(Nombre) FROM proyecto_sentiments2.author;"))
    lista =  [{"nombre": elemento[0]} for elemento in query]
    return lista


def get_quotes():
    query= list(engine.execute("SELECT (Frases) FROM proyecto_sentiments2.quotes;"))
    lista_frases =  [{"frase": elemento[0]} for elemento in query]
    return lista_frases


def frases_porautor(autor): 
    query = pd.read_sql_query(f"""
    SELECT q.Frases, a.Nombre
    FROM quotes as q
    INNER JOIN author as a
    ON a.idAutor=q.AUTHOR_idAutor
    WHERE Nombre='{autor}';
    """,engine).to_json(orient="records")
    return query


def frase_porgenero(genero):
    query = pd.read_sql_query(f"""
    SELECT q.Frases, g.Genre
    FROM quotes as q
    INNER JOIN genre as g
    ON g.idGenre=q.GENRE_idGenre
    WHERE Genre='{genero}';
    """,engine).to_json(orient="records")
    return query


def random_quote():
    query= list(engine.execute("SELECT (Frases) FROM proyecto_sentiments2.quotes;"))
    lista_f =  [{"La frase del día es": elemento[0]} for elemento in query]
    hoy=str(datetime.today())
    ran={hoy: random.choice(lista_f)} 
    return ran


def traslation(quote):
    query= list(engine.execute("SELECT (Frases) FROM proyecto_sentiments2.quotes;"))
    translator = Translator()
    lista_frases =  [{"frase traducida": translator.translate( elemento[0])} for elemento in query]
    return lista_frases