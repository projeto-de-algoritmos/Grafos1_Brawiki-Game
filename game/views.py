from django.shortcuts import render
from bs4 import BeautifulSoup
from scripts import bfs

def add_attr_html(page, source, target, num_clicks, my_path):
    html_page = bfs.get_html_page(page)
    soup = BeautifulSoup(html_page, 'html.parser')
    links = soup.find_all('a')
    for link in links:
        href = link.get('href')
        if href:
            link['href'] = f"{href}?source={source}&target={target}&num_clicks={num_clicks}&my_path={my_path}"

    return str(soup)

def index(request):
    default_img = "/static/game/img/default-img.svg"
    nodes = bfs.get_nodes()

    source_img = bfs.get_page_thumb(nodes[0]) or default_img
    target_img = bfs.get_page_thumb(nodes[1]) or default_img

    context = {
        'tempo_inicial': 100,
        'source': nodes[0],
        'target': nodes[1],
        'source_img': source_img,
        'target_img': target_img
    }

    return render(request, "game/index.html", context)

def round(request, page):
    source = request.GET.get('source')
    target = request.GET.get('target')
    num_clicks = int(request.GET.get('num_clicks')) + 1
    my_path = request.GET.get('my_path') + page.replace('_', ' ') + ','

    if target == page.replace('_', ' '):
        html_page = bfs.get_html_page(page)
        html_page = add_attr_html(page, source, target, num_clicks, my_path)

        shortest_path = bfs.getGraphShortestPath(source, target)
        shortest_path = ' ⮕ '.join(shortest_path)

        my_path = my_path.strip(',').replace(',', ' ⮕ ')
        
        if my_path.count('⮕') == shortest_path.count('⮕'):
            title_path = "Caminho alternativo:"
        else:
            title_path = "Caminho mais curto:"

        context = {
            'source': source,
            'target': target,
            'html_page': html_page,
            'num_clicks': num_clicks,
            'shortest_path': shortest_path,
            'my_path': my_path,
            'title_path': title_path,
            'target_found': True,
        }
    else:
        html_page = add_attr_html(page, source, target, num_clicks, my_path)
        context = {
            'source': source,
            'target': target,
            'html_page': html_page,
            'num_clicks': num_clicks,
            'shortest_path': "",
            'my_path': my_path.replace(',', ' ⮕ '),
            'target_found': False,
        }

    return render(request, "game/round.html", context)
