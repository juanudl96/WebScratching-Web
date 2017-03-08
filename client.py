#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8 :

'''
Client web per www.packtpub.com/packt/offers/free-learning

@author juanbone16@gmail.com'''

import urllib2
from bs4 import BeautifulSoup

#TODO: coses a fer
#FIXME: coses a arreglar
#Només volem els comentaris necessaris. A la linea web = self.get_web no cal comentari perque ja es veu el que fa la funcio.

class Client(object):
    def get_web(self,page):
        """baixar-se la web"""          #documentacio de la funcio
        f = urllib2.urlopen(page)
        html = f.read()                 #cadena de text amb tot el contingut del fitxer.
        f.close()
        return html


    #buscar el text
    def search_text(self,html):
        soup = BeautifulSoup(html, 'html.parser')
        elements = soup.find("div" , "dotd-title")
        resultats = elements.find("h2")
        #for element in elements:
        #    title = element.find("h2")
        #    resultats.append(title)
        return resultats.text if resultats else "Error"

    # def borrar_caracters(self,resultats):
    #    BORRAR = ['\n','\t']
    #    for caracter in BORRAR:
    #        resultats = resultats.replace(caracter,"")
    #    return text

    def main(self):
        web = self.get_web('https://www.packtpub.com/packt/offers/free-learning')
        resultat = self.search_text(web)
        resultat = resultat.replace("\n","").replace("\t","")
        #imprimir resultats sense salts de linea
        # resultat = self.borrar_caracters(resultat)

        print resultat

if __name__=="__main__":
    client=Client()
    client.main()
