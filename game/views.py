from django.shortcuts import render
from scripts import bfs


def index(request):
    tempo_inicial = "gl"
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
        'tempo_inicial': tempo_inicial,
        'source': nodes[0],
        'target': nodes[1],
        'source_img': source_img,
        'target_img': target_img
    }
    
    return render(request, "game/index.html", context)

def round(request):
    source = request.GET.get('source')
    target = request.GET.get('target')

    html_page = bfs.get_html_page(source)

    context = {
        'source': source,
        'target': target,
        'source_url': source.replace(' ', '_'),
        'html_page': html_page
    }

    print(source, target)
    return render(request, "game/round.html", context)
