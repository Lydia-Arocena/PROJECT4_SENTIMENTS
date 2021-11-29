from config.configuration import engine

def remplazo_comas(frase):
    """
    Sustituye los ' por `.
    """
    sin_comas=frase.replace("'","`")
    return sin_comas



def getId(tabla,string):
    """
    Devuelve el ID de lo que le pidamos.
    """
    if tabla == "author":
        return list(engine.execute(f"SELECT idautor FROM author WHERE nombre ='{string}';"))[0][0]
    elif tabla == "genre":
        return list(engine.execute(f"SELECT idGenre FROM genre WHERE genre ='{string}';"))[0][0]



def replace_author_id(x):
    """
    Devuelve una lista de ids de autores cuando le paso los nombres de los mismos.
    """

    for au in range(len(autores_id)):
        if x == (autores_id[au][1]):
            return autores_id[au][0]


def replace_genre_id(x):
    """
    Devuelve una lista de ids de los géneros cuando le paso los nombres de los mismos.
    """

    for g in range(len(genre_id)):
        if x == (genre_id[g][1]):
            return genre_id[g][0]