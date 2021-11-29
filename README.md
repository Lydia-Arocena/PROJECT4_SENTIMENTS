# PROYECTO4_SENTIMENTS

![imagen](https://github.com/Lydia-Arocena/PROYECTO4_SENTIMENTS/blob/main/foto_quote.png)

# Creando una API de Frases célebres:
En este proyecto he creado una API que permite obtener información de una base de datos (MySQL) sobre frases célebres de multitud de autores y los géneros a las que pertenecen.

Analizando sentimientos de cada uno de los autores con TextBlob y NLP (procesamiento del lenguaje natural) en Python.

### ¿Cómo funciona?
## @get

- /autores

Con este endpoint obtenemos todos los autores.
```
url = "http://127.0.0.1:5000/autores"
requests.get(url).json()
```
- /frases

Con este endpoint obtenemos todas las frases.
```
url = "http://127.0.0.1:5000/frases"
requests.get(url).json()
```
- /frases/name

Con este endopoint obtenemos todas las frases del autor que le indiquemos.
```
url = f"http://127.0.0.1:5000/frases/{autor}"
autor = "Voltaire"
requests.get(url + autor).json()
```
- /frases_g/genero

Con este endpoint obtenemos todas las frases del género que le indique el usuario.
```
url = f"http://127.0.0.1:5000/frases_g/{genero}"
genero = "age"
requests.get(url + genero).json()
```
- /random

Con este endpoint obtenemos la frase del día: frase aleatoria junto a la fecha y hora del momento en el que hagamos la llamada a la API.
```
url = "http://127.0.0.1:5000/random"
requests.get(url).json()

```
- /frases_/genero/autor

Con este endpoint obtenemos una frase aleatoria de un autor y género concretos que le pasemos.
```
url = f"http://127.0.0.1:5000/frases_/{genero}/{autor}"
genero="age"
autor="Voltaire"
requests.get(url + genero + autor).json()
```

- /frases_lan/genero/autor

Con este endpoint obtenemos una frase aleatoria de un autor y género concretos que le pasemos y tenemos la opción de que nos la traduzca a otro idioma si le pasamos el idioma como parámetro opcional.
```
url= f"http://127.0.0.1:5000/frases_lan/{genero}/{autor}?idioma={idioma}"
genero="age"
autor="Voltaire"
idioma="es"
requests.get(url + genero + autor + idioma).json()
```

- /NLP/autor

Análisis de sentimientos: Analizamos la polaridad de las frases del autor que le pasemos.
```
url=f"http://127.0.0.1:5000/NLP/{autor}"
autor="Emily Carr"
requests.get(url + autor).json()
```


## @post

- /nuevafrase

Nos permite insertar frases nuevas en la base de datos realizando una request.post a la API como en el siguiente ejemplo. 

```
quote={"author":17, "genre":52, "quote":"In joined hands there is still some token of hope, in the clenched fist none"}
url = "http://127.0.0.1:5000/nuevafrase"
requests.post(url, data=quote)
```

- /nuevoautor

Nos permite insertar un autor nuevo en la base de datos realizando una request.post a la API como en el siguiente ejemplo. 

```
autor= {"author":"Calderón de la Barca"}
url = "http://127.0.0.1:5000/nuevoautor"
requests.post(url, data=autor)
```

