import requests
from bs4 import BeautifulSoup


#localfile = open("home.html") # <- carga archivo local para scrap
link = "https://github.com/xspark21/web-scraping"

# faltaria añadirle la funcionalidad de abrir archivos locales tambien
def scrap(url,struct,tag):
    """
    Args:
    url: enlace de la pagina a escrapear
    struct: estructura del html en donde buscar
    tag: etiqueta a buscar  
    """
    html = BeautifulSoup(requests.get(url).text, 'html.parser')
    tags = html.select(f"{struct} {tag}")
    print(f"hay {len(tags)} {tag} en el {struct}")
    return html, tags


document , etiquetas = scrap(link,"body","div")

