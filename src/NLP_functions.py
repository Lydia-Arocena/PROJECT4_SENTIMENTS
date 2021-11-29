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
    query = pd.read_sql_query(f"""
    SELECT q.Frases
    FROM quotes as q
    INNER JOIN author as a
    ON a.idAutor=q.AUTHOR_idAutor
    WHERE Nombre='{autor}';
    """,engine)
    return query


def NLP_tokenizer(query):
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
    sia = SentimentIntensityAnalyzer()
    polaridad = sia.polarity_scores(quote)
    pol = polaridad["compound"]
    return pol