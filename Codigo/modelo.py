#!/usr/bin/env python
# -*- coding: utf-8 -*-

import preprocesoTweets as pt
import collections
import numpy as np


def contruirVocab(listoffiles):
    voc=set()
    bowmodel=collections.Counter()
    lemas=[]
    for f in listoffiles:
        v,b,l=pt.preprocesar(f)
        voc.update(v)
        bowmodel.update(b)
        lemas=lemas+l
    return sorted(voc),b,lemas

def construirVector(tweet,c):
    vecc=[]
    for i in range(len(c)):
        if c[i][0] in tweet:
            vecc.append(1)
        else:
            vecc.append(0)
    return vecc

def construirMat(ts,c):
    m=[]
    print len(ts)
    for i in range(len(ts)):
        m.append(construirVector(ts[i],c))
    return np.array(m)

def vocabularioTotal():
    a=['Santos.txt','Zuluaga.txt','ClaraLopez.txt','MartaLuciaRamirez.txt','Penalosa.txt','DataSet.txt']
    v,b,l=contruirVocab(a)
    return v,b,l


##print len(v)
## graficamos las palabras totales del documento
##l=pt.graficar(b)
##print b
##caracteristica=b.most_common(1000)
##M=construirMat(l,caracteristica)
## guardamos la matriz de caracteristicas
##np.save("DataSet.npy",M)


