import queue
import random
import requests
import json
import wikipediaapi
from pilot import *

shortestPath = []
def get_nodes():
    try:
        with open("../data/pt-wiki-pages-final.txt", 'r') as file:
            lines = file.readlines()

        nodes = [line.strip() for line in random.sample(lines, 2)]

        return nodes

    except FileNotFoundError:
        return None 

def build_graph():
    graph = {}
    with open('../data/pt-wiki-edges-final.txt', 'r' ,encoding='utf-8') as file:
        for line in file:
            key, neighbors_str = line.strip().split(':', 1)
            neighbors = [neighbor.strip() for neighbor in neighbors_str.strip('[]').split(',')]
            neighbors_no_quotes = [elem.strip("'") for elem in neighbors]
            graph[key] = neighbors_no_quotes
    return graph

def bfs(graph, source, target):
    if source not in graph or target not in graph:
        return None 

    fila = queue.Queue()
    visited = set()
    fila.put((source, [source]))

    while not fila.empty():
        (node, path) = fila.get()
        if node == target:
            return path
        if node not in visited:
            visited.add(node)
            if node in graph:
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        fila.put((neighbor, path + [neighbor]))
    return None 

def get_page_thumb(search_term):
    WIKI_REQUEST = 'https://pt.wikipedia.org/w/api.php?action=query&formatversion=2&format=json&&pithumbsize=250&prop=pageimages&titles='
    try:
        response  = requests.get(WIKI_REQUEST+search_term)
        json_data = json.loads(response.text)
        img_link = json_data['query']['pages'][0]['thumbnail']['source']
        return img_link        
    except:
        return None

def getGraphShortestPath():

    path = bfs(build_graph(), "Guilherme Bellintani", "Saci")
    
    pilot(path)
    


getGraphShortestPath()
