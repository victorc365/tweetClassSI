#!/usr/bin/env python
# -*- coding: utf-8 -*-

import nltk

###leer los ficheros de tweets

def leerFichero(nombreFichero):
    f=open(nombreFichero,'r')
    tweets=[]
    linea=f.readline()
    tweets.append(linea)
    while linea !="":
        linea=f.readline()
        tweets.append(linea)
    print len(tweets)
    print tweets


leerFichero("Santos.txt")
