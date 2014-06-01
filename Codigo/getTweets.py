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
    tweets=api.GetSearch(term=subject,lang="es");
    for tweet in tweets:
        print tweet.text
        print "-----------------------------------"

# Llamada a la funcion

getTweetsAboutSubject("Messi",api);
    
