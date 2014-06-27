#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pylab as pl
import numpy as np
import modelo as mdl
import preprocesoTweets as pt
import collections

def cargarResultados(filename):
    return np.load(filename)


def posicionTporcandidato(ts):
    indices=[]
    for i in range(len(ts)):
        if not ts[i]:
            indices.append(i)
    return indices

def organizarPorClase(ts,labels):
    c1=[]
    c2=[]
    c3=[]
    c4=[]
    c5=[]
    for i in range(len(ts)):
        if labels[i]==0:
            c1.append(ts[i])
        elif labels[i]==1:
            c2.append(ts[i])
        elif labels[i]==2:
            c3.append(ts[i])
        elif labels[i]==3:
            c4.append(ts[i])
        else:
            c5.append(ts[i])
    return c1,c2,c3,c4,c5

def palabrasMascomunes(clase):
    sumbag=sum(clase,collections.Counter())
    return sumbag

resultados=cargarResultados('resultados.npy')
a=['Santos.txt','Zuluaga.txt','ClaraLopez.txt','MartaLuciaRamirez.txt','Penalosa.txt','DataSet.txt']
v,b,l=mdl.contruirVocab(a)
tweets=l
Santos=tweets[:130]
Zuluaga=tweets[132:253]
Clara=tweets[255:377]
Marta=tweets[379:537]
Penalosa=tweets[539:]
indices=posicionTporcandidato(tweets)
SantosClass=collections.Counter(resultados[0][:130])
ZuluagaClass=collections.Counter(resultados[0][132:253])
ClaraClass=collections.Counter(resultados[0][255:377])
MartaClass=collections.Counter(resultados[0][379:537])
PenalosaClass=collections.Counter(resultados[0][539:])

def graf(cl):
    altura=cl.values()
    etiquetas=cl.keys()
    X=np.arange(len(altura))
    pl.bar(X,altura,facecolor='#0000FF',edgecolor='black')
    i=0
    for x,y in zip(X,altura):
        pl.text(x+0.4,y+0.5,str(etiquetas[i]),ha='center',va='bottom')
        i+=1
    pl.show()


##graf(PenalosaClass)
##c1,c2,c3,c4,c5=organizarPorClase(tweets,resultados[0])
##b=pt.bow(c5)
##bows=pt.bowDocumento(b[0])
##pt.graficar(bows)
