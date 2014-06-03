#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pymongo import MongoClient
import twitter

# Datos de autenticación
OAUTH_TOKEN="241216389-m1AsDOevhm1G9FV5hS8kxqqr9BgUAZxGJxSISiA6"
OAUTH_SECRET="X4vJ72EaZymWPyD5PHRWqcxA7Udjfzpu221haoJjxoBTR"
CONSUMER_KEY="B5E0KOb0zf2PU1RapGne5qjMA"
CONSUMER_SECRET="i3AaYnmcb0f2UFzoac7BoOgzYq4xgUSoVKvFlqGaAPJhzWhJgn"

# Conexion a la Api
api=twitter.Api(consumer_key=CONSUMER_KEY,
                consumer_secret=CONSUMER_SECRET,
                access_token_key=OAUTH_TOKEN,
                access_token_secret=OAUTH_SECRET);

#obtenemos los tweets
def getTweetsAboutSubject(subject,api):
    tweets=api.GetSearch(term=subject,lang="es",count="100");
    return tweets

# obtener tweets de un solo usuario
def getUserTimeLine(userId,api):
    statuses=api.GetUserTimeline(userId)
    print[s.text for s in statuses]
# Llamada a la funcion

tweets1=getTweetsAboutSubject("salud",api);

f=open("DataSet.txt","a")
for t in tweets1:
    f.write(str(t.text.encode('utf-8'))+"\n")

tweets1=getTweetsAboutSubject("educacion",api);
for t in tweets1:
    f.write(str(t.text.encode('utf-8'))+"\n")
tweets1=getTweetsAboutSubject("seguridad",api);
for t in tweets1:
    f.write(str(t.text.encode('utf-8'))+"\n")
tweets1=getTweetsAboutSubject("empleo",api);
for t in tweets1:
    f.write(str(t.text.encode('utf-8'))+"\n")
tweets1=getTweetsAboutSubject("paz",api);
for t in tweets1:
    f.write(str(t.text.encode('utf-8'))+"\n")
f.close()


    
