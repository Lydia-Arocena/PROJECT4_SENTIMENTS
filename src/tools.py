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


def random_aut_gen(genero, autor):
    query = list(engine.execute(f"""
    SELECT q.Frases
    FROM author as a
    INNER JOIN quotes as q
    ON a.idAutor=q.AUTHOR_idAutor
    INNER JOIN genre as g
    ON g.idGenre=q.GENRE_idGenre
    WHERE Genre='{genero}'and Nombre='{autor}';
    """))
    lista_r =  [{"esta ": elemento[0]} for elemento in query]
    frase_random=random.choice(lista_r)
    dicc_ =  {f"La frase de '{autor}' sobre '{genero}' es ": frase_random}
    return dicc_


def random_aut_gen_2(lang, genero, autor):
    trans = Translator()
    if lang == "en":
        return random_aut_gen(genero, autor)
    elif lang == "es":
        sintraducir = random_aut_gen(genero, autor)
        traducido = trans.translate(random_aut_gen(genero,autor), dest="es").text
        return f"Traducción: {traducido}"
    else:
        return random_aut_gen(genero, autor)
    
