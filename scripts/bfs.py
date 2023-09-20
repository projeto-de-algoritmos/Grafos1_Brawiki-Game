import queue

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


graph = {}

with open('data/pt-wiki-edges-final.txt', 'r') as file:
    for line in file:
        key, neighbors_str = line.strip().split(':', 1)
        neighbors = [neighbor.strip() for neighbor in neighbors_str.strip('[]').split(',')]
        neighbors_no_quotes = [elem.strip("'") for elem in neighbors]
        graph[key] = neighbors_no_quotes

source = "Babalorixá"
target = "Saci"

path = bfs(graph, source, target)

if path:
    print(f"Menor path entre {source} e {target}: {path}")
else:
    print(f"Não foi encontrado um path entre {source} e {target}")
