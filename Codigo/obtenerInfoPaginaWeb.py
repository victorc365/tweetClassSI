#-*- coding:utf-8 -*-

from BeautifulSoup import BeautifulSoup
import urllib2

# Obtiene el titulo de una pagina web
def obtener_titulo(url):
    page=urllib2.urlopen(url)
    soup=BeautifulSoup(page)
##    print (soup.getText())
    entrada=None 
    for division in soup.fetch('div'):
        idntifica=division.get('id')
        if idntifica=="resultado":
            entrada=soup.find(id="resultado")
            entrada=entrada.getText()
    return entrada


if __name__=="__main__":
    url="http://diccionario.terra.com.ar/diccionario/mentira"
    print obtener_titulo(url)
    
    
