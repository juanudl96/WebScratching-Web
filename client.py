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
        elements = soup.find_all("div" , "dotd-title")
        resultats = []
        for element in elements:
            title = element.find("h2")
            resultats.append(title)
        return resultats

    def main(self):
        web = self.get_web('https://www.packtpub.com/packt/offers/free-learning')
        resultat = self.search_text(web)
        #imprimir resultats
        print resultat

if __name__=="__main__":
    client=Client()
    client.main()
