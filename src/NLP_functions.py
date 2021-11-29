from config.configuration import engine
import pandas as pd
import re
import string
import spacy
import en_core_web_sm
from nltk.corpus import stopwords
from textblob import TextBlob
import nltk
nltk.downloader.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def NLP_createdf(autor): 
    """
    Esta función me crea un df con las frases del autor que le paso como argumento.
    """
    query = pd.read_sql_query(f"""
    SELECT q.Frases
    FROM quotes as q
    INNER JOIN author as a
    ON a.idAutor=q.AUTHOR_idAutor
    WHERE Nombre='{autor}';
    """,engine)
    return query


def NLP_tokenizer(query):
    """
    Esta función tokeniza la frase que le pasamos como argumento, es decir, extrae las palabras relavantes para hacer el análisis de sentimientos.
    """
    nlp = spacy.load("en_core_web_sm")
    tokens = nlp(query)
    filtradas = []
    for token in tokens:
        if not token.is_stop:
            lemma = token.lemma_.lower().strip()
            if re.search('^[a-zA-Z]+$',lemma): 
                filtradas.append(lemma)
    return " ".join(filtradas)


def NLP_sentiment(quote):
    """
    Esta función me devuelve la polaridad de la frase que le paso como argumento.
    """
    sia = SentimentIntensityAnalyzer()
    polaridad = sia.polarity_scores(quote)
    pol = polaridad["compound"]
    return pol