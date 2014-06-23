#!/usr/bin/env python
# -*- coding: utf-8 -*-

import nltk
import re
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
import unicodedata


###leer los ficheros de tweets y tokeniza en palabras

def leerFichero(nombreFichero):
    ## Lee los tweets linea a linea desde un fichero txt
    ## abre el fichero en modo lectura 
    f=open(nombreFichero,'r')
    ## lista que guardará los tweets recuperados
    tweets=[]
    ## leemos la primera linea del fichero
    linea=f.readline()
    ## la decodificamos para obtener los caracteres Unicode
    linea=linea.decode(encoding='utf8',errors='ignore')
    ## agregamos la linea a la lista
    tweets.append(linea)
    ## realizamos el bucle hasta llegar al final del mismo
    while linea !="":
        ## leemos la siguiente linea
        linea=f.readline()
        ## la decodificamos
        linea=linea.decode(encoding='utf8',errors='ignore')
        ## ignoramos las lineas vacias
        if linea!='\n':
        ## agregamos la linea a la lista
            tweets.append(linea)
    ## retornamos la lista 
    return tweets

def eliminarLinks(ListTweets):
    ## recibe como parametro una lista de tweets
    ## Guardara los tweets sin hipervinculos
    tweetp=[]
    ## crea el patron a reemplazar en cada tweet
    pattern='https?://\S+'
    ## compila el patron a buscar
    p=re.compile(pattern)
    ## recorre la lista de tweets
    for t in ListTweets:
        ## elimina el link del tweet
        t=re.sub(p,'',t)
        ## agrega la linea preprocesada 
        tweetp.append(t)
    ## retorna los tweets preprocesados
    return tweetp 
        
def eliminarStopWords(lstoftokens):
    ## signos de twitter
    s=set(['rt','@','#','.',',',';',':','!','?','¿'])
    ## stop words
    sw=set(stopwords.words('spanish'))
    sw.update(s) ##union de los dos conjuntos
    filtered_words=[]
    for f in lstoftokens:
        filtered_words.append([w.lower() for w in f if not w.lower() in sw])
    return filtered_words
    

def tokenizar(listTweets):
    ## recibe una lista de tweets y devuelve la lista tokenizada por palabras
    tokens=[]
    for t in listTweets:
        ## normalizamos las palabras
        tokens.append(nltk.word_tokenize(t))
    return tokens


def lematizador(listofwords):
    spanish_stemmer=SnowballStemmer("spanish")
    lemas=[]
    for p in listofwords:
        lemas.append([spanish_stemmer.stem(t) for t in p])
    return lemas

def elimina_tildes(cadena):
    ## elimina las tildes debe entrar un unicode data u
    s=''.join((c for c in unicodedata.normalize('NFD',cadena) if unicodedata.category(c)!='Mn'))
    return s
    
listTT=leerFichero("Santos.txt")
listTT=eliminarLinks(listTT)
token=tokenizar(listTT)
token=eliminarStopWords(token)
lema=lematizador(token)
print lema

