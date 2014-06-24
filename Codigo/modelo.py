#!/usr/bin/env python
# -*- coding: utf-8 -*-

import preprocesoTweets as pt
import collections



def contruirVocab(listoffiles):
    voc=set()
    for f in listoffiles:
        v=pt.preprocesar(f)
        voc.update(v)
    return sorted(voc)

a=['Santos.txt','Zuluaga.txt','ClaraLopez.txt','MartaLuciaRamirez.txt','Penalosa.txt','DataSet.txt']
v=contruirVocab(a)
print len(v)



