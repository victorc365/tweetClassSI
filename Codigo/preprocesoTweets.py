#!/usr/bin/env python
# -*- coding: utf-8 -*-

import nltk
import re
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from matplotlib.pylab import hist, show
import matplotlib as plt
import unicodedata
import collections
import numpy as np
import pylab as pl

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
    ## elimina las tildes
    linea=elimina_tildes(linea)
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

def elimina_tildes(cadena):
    ## elimina las tildes debe entrar un unicode data u
    s=''.join((c for c in unicodedata.normalize('NFD',cadena) if unicodedata.category(c)!='Mn'))
    return s

def eliminarLinks(ListTweets):
    ## recibe como parametro una lista de tweets
    ## Guardara los tweets sin hipervinculos
    tweetp=[]
    ## crea el patron a reemplazar en cada tweet
    pattern='https?://\S+'
    p2='[0-9]+'
    ## compila el patron a buscar
    p=re.compile(pattern)
    ## recorre la lista de tweets
    for t in ListTweets:
        ## elimina el link del tweet
        t=re.sub(p,'',t)
        t=re.sub(p2,'',t)
        ## agrega la linea preprocesada 
        tweetp.append(t)
    ## retorna los tweets preprocesados
    return tweetp 
        
def eliminarStopWords(lstoftokens):
    ## signos de twitter
    s=set(['rt','@','#','.',',',';',':','!','?','¿','+','-','..','...',"'","''","uy",u'``',')','(',u'mas' \
           u'q','&','c','http','|','mas',u'\u2026'])
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

def vocabulario(words):
    vocad=set()
    for f in words:
        vocad.update([w for w in f])
    return vocad

def bow(listlema):
    bagofwords=[]
    bagofwords.append([collections.Counter(p) for p in listlema])
    return bagofwords

def bowDocumento(bagw):
    sumbag=sum(bagw,collections.Counter())
    return sumbag

def graficar(sumbag):
    mostcommon=sumbag.most_common(8)
    labels=[]
    valores=[]
    del(mostcommon[0])
    for i in range(len(mostcommon)):
        labels.append(mostcommon[i][0].encode('utf-8','ignore'))
        valores.append(mostcommon[i][1])
    X=np.arange(len(mostcommon))
    pl.bar(X,valores,facecolor='#0000FF',edgecolor='black')
    ## nombrar ejes
    pl.xlabel('palabras mas comunes')
    pl.ylabel('frecuencia de palabra')
    ##colocar texto
    i=0
    for x,y in zip(X,valores):
        pl.text(x+0.4,y+0.5,labels[i],ha='center',va='bottom')
        i+=1
    pl.show()
    return labels


def preprocesar(fileName):
    listTT=leerFichero(fileName)
    listTT=eliminarLinks(listTT)
    token=tokenizar(listTT)
    token=eliminarStopWords(token)
    lema=lematizador(token)
    voc=vocabulario(lema)
    b=bow(lema)
    sumba=bowDocumento(b[0])
    return voc,sumba,lema
    
##print len(voc)
##print b
##v,sumba,lema=preprocesar('MartaLuciaRamirez.txt')
##l=graficar(sumba)
##print l
    

