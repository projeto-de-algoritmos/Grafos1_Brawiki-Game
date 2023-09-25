from django.shortcuts import render
from bs4 import BeautifulSoup
from scripts import bfs

def add_attr_html(page, source, target):
    html_page = bfs.get_html_page(page)
    soup = BeautifulSoup(html_page, 'html.parser')
    links = soup.find_all('a')
    for link in links:
        href = link.get('href')
        if href:
            link['href'] = f"{href}?source={source}&target={target}"
    return str(soup)

def index(request):
    default_img = "/static/game/img/default-img.svg"
    graph = bfs.build_graph()
    nodes = None
    path = None

    while path is None:
        nodes = bfs.get_nodes()
        path = bfs.bfs(graph, nodes[0], nodes[1])

    source_img = bfs.get_page_thumb(nodes[0]) or default_img
    target_img = bfs.get_page_thumb(nodes[1]) or default_img

    context = {
        'tempo_inicial': "gl",
        'source': nodes[0],
        'target': nodes[1],
        'source_img': source_img,
        'target_img': target_img
    }

    return render(request, "game/index.html", context)

def round(request, page):
    source = request.GET.get('source')
    target = request.GET.get('target')

    if target == page.replace('_', ' '):
        html_page = bfs.get_html_page(page)
        html_page = add_attr_html(page, source, target)
        context = {
            'source': source,
            'target': target,
            'html_page': html_page,
            'target_found': True
        }
    else:
        html_page = add_attr_html(page, source, target)
        context = {
            'source': source,
            'target': target,
            'html_page': html_page,
            'target_found': False
        }

    return render(request, "game/round.html", context)
