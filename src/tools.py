from config.configuration import engine
import pandas as pd
import random
from datetime import datetime
from googletrans import Translator




def get_autores():
    """
    Esta función me devuelve una lista de todos los autores de mi base de datos.
    Args: ninguno.
    Return: lista autores.
    
    """
    query = list(engine.execute("SELECT distinct(Nombre) FROM proyecto_sentiments2.author;"))
    lista =  [{"nombre": elemento[0]} for elemento in query]
    return lista


def get_quotes():
    """
    Esta función me devuelve una lista de todas las frases de mi base de datos.
    Args: ninguno.
    Return: lista de frases.
    
    """
    query= list(engine.execute("SELECT (Frases) FROM proyecto_sentiments2.quotes;"))
    lista_frases =  [{"frase": elemento[0]} for elemento in query]
    return lista_frases


def frases_porautor(autor): 
    """
    Esta función me devuelve un json de todas las frases del autor que le pase.
    Args: autor(string).
    Return: json de frases del autor pasado como argumento.
    """
    query = pd.read_sql_query(f"""
    SELECT q.Frases, a.Nombre
    FROM quotes as q
    INNER JOIN author as a
    ON a.idAutor=q.AUTHOR_idAutor
    WHERE Nombre='{autor}';
    """,engine).to_json(orient="records")
    return query


def frase_porgenero(genero):
    """
    Esta función me devuelve un json de todas las frases del género que le pase.
    Args: género(string).
    Return: json de frases del género pasado como argumento.
    """
    query = pd.read_sql_query(f"""
    SELECT q.Frases, g.Genre
    FROM quotes as q
    INNER JOIN genre as g
    ON g.idGenre=q.GENRE_idGenre
    WHERE Genre='{genero}';
    """,engine).to_json(orient="records")
    return query


def random_quote():
    """
    Esta función me devuelve una frase al azar.
    Args: ninguno.
    Return: frase (string)
    """
    query= list(engine.execute("SELECT (Frases) FROM proyecto_sentiments2.quotes;"))
    lista_f =  [{"La frase del día es": elemento[0]} for elemento in query]
    hoy=str(datetime.today())
    ran={hoy: random.choice(lista_f)} 
    return ran


def random_aut_gen(genero, autor):
    """
    Esta función me devuelve una frase al azar de un autor y género concreto.
    Args: genero (string).
          autor (string).
    Return: frase (string)
    """
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
    """
    Esta función devuelve una frase al azar de un autor y género determinado traducida al español.
    Args: lang (string)
          genero (string)
          autor (string)
    Return: frase traducida.
    """
    trans = Translator()
    if lang == "en":
        return random_aut_gen(genero, autor)
    elif lang == "es":
        traducido = trans.translate(random_aut_gen(genero,autor), dest="es").text
        return f"Traducción: {traducido}"
    else:
        return random_aut_gen(genero, autor)
    


def nuevafrase(author, genre, quote):

    """
    Esta función introduce una nueva frase a la base de datos.
    Args: author (string)
          genre (string)
          quote (string)
    Return: frase introducida.
    """
    engine.execute(f"""
    INSERT INTO quotes (AUTHOR_idAutor, GENRE_idGenre, Frases)
    VALUES ({author}, '{genre}', '{quote}');
    """)
    return f"Se ha introducido correctamente: {author} {genre} {quote}"


def nuevoautor(author):
    """
    Esta función introduce un nuevo autor a la base de datos.
    Args: author (string)
    Return: autor nuevo introducido.
    """
    engine.execute(f"""
    INSERT INTO author(Nombre)
    VALUES ('{author}');
    """)
    return f"Se ha introducido correctamente el : {author}"
