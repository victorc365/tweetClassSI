#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os
import re
import unicodedata
import nltk

def leerarchivo(nombrearchivo):
    archivo=open(nombrearchivo,'r')
    lineas=archivo.readlines()
    s=''
    tweets=[]
    for li in lineas:
        if not li=='\\n':
            li=li.decode(encoding='utf8',errors='ignore')
            ## eliminamos las tildes y caracteres extraños
            li=elimina_tildes(li)
            li=re.sub('\n','',li)
            s.join(li)
        else:
            tweets.append(s)
            s=''
    return tweets


def elimina_tildes(cadena):
    ## elimina las tildes debe entrar un unicode data u
    s=''.join((c for c in unicodedata.normalize('NFD',cadena) if unicodedata.category(c)!='Mn'))
    return s

def datos_de_textos(nombre_archivo):
    f=open(nombre_archivo)
    raw=f.read()
    raw=raw.decode(encoding='utf8',errors='ignore')
    raw=elimina_tildes(raw)
    tokens=nltk.wordpunct_tokenize(raw)
    text=nltk.Text(tokens)
    return text


texto=datos_de_textos('Santos.txt')
## distribucion de frecuencias
fdist=nltk.probability.FreqDist(texto)
voca=fdist.samples()
print fdist.max()


    
    
