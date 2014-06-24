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
    for i in range(len(ts)):
        m.append(construirVector(ts[i],c))
    return np.array(m)
        
a=['Santos.txt','Zuluaga.txt','ClaraLopez.txt','MartaLuciaRamirez.txt','Penalosa.txt','DataSet.txt']
v,b,l=contruirVocab(a)
print len(v)
##print b
caracteristica=b.most_common(100)
M=construirMat(l,caracteristica)
np.save("DataSet.npy",M)


