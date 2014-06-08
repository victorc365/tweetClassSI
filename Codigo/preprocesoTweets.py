#!/usr/bin/env python
# -*- coding: utf-8 -*-

import nltk
import re

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
        
def eliminarStopWords(stopWords,listaAprocesar):
    ## eliminado de hipervinculos
    tokens=[]
    tokens.append(nltk.word_tokenize(linea))
    for i in range(len(listaAprocesar)):
        for j in range(len(listaAprocesar[i])):
            if re.search('^https?://',listaAprocesar[i][j]):
                del listaAprocesar[i][j]

def tokenizar(listTweets):
    ## recibe una lista de tweets y devuelve la lista tokenizada por palabras
    tokens=[]
    for t in listTweets:
        tokens.append(nltk.word_tokenize(t))
    return tokens
        
    

    
listTT=leerFichero("Santos.txt")
listTT=eliminarLinks(listTT)
token=tokenizar(listTT)
##eliminarStopWords('',listTT)
print token

