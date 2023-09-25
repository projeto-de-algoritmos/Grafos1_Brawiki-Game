from bs4 import BeautifulSoup
import queue
import requests
import json
# from scripts.pilot import *


# shortestPath = []
def get_page_thumb(search_term):
    WIKI_REQUEST = 'https://pt.wikipedia.org/w/api.php?action=query&formatversion=2&format=json&&pithumbsize=250&prop=pageimages&titles='
    try:
        response  = requests.get(WIKI_REQUEST+search_term)
        json_data = json.loads(response.text)
        img_link = json_data['query']['pages'][0]['thumbnail']['source']
        return img_link        
    except:
        return None

def get_html_page(search_term):
    WIKI_REQUEST = "https://pt.wikipedia.org/w/api.php?action=parse&format=json&page="

    try:
        response = requests.get(WIKI_REQUEST + search_term)
        json_data = response.json()
        html = json_data['parse']['text']['*']

        soup = BeautifulSoup(html, 'html.parser')

        for tag in soup.find_all(class_=["mw-editsection", "external", "reference", "reflist", "Ligações_externas", "plainlinks"]):
            tag.decompose()

        for tag in soup.find_all():
            for attr_name, attr_value in tag.attrs.items():
                if 'Wikipédia:' in attr_value:
                    tag.extract()
        
        tags_to_remove = soup.find_all(href=lambda href: href and 'Ficheiro:' in href)
        for tag in tags_to_remove:
            tag.attrs.pop('href', None)

        for id_to_remove in ["Referências", "Ligações_externas"]:
            for tag in soup.find_all(id=id_to_remove):
                tag.extract()

        return str(soup)

    except:
        return None

# def getGraphShortestPath():

#     path = bfs(build_graph(), "Guilherme Bellintani", "Saci")
#     pilot(path)

# getGraphShortestPath()
