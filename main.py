#import requests
from urllib.request import urlopen 
from bs4 import BeautifulSoup

filehandle = open("home.html")

html = urlopen('https://www.mappa.co.jp/en/')
soup = BeautifulSoup(html, 'html.parser')

#print(soup.prettify())

print(soup.div) 
