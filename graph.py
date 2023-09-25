import random
import queue

class Graph:
    def __init__(self):
        self.graph = self.build_graph()

    def build_graph(self):
        graph = {}
        with open('data/pt-wiki-edges-final.txt', 'r', encoding='utf-8') as file:
            for line in file:
                key, neighbors_str = line.strip().split(':', 1)
                neighbors = [neighbor.strip() for neighbor in neighbors_str.strip('[]').split(',')]
                neighbors_no_quotes = [elem.strip("'") for elem in neighbors]
                graph[key] = neighbors_no_quotes
        return graph

    def dfs(self, start, end):
        visited = set()
        stack = [start]

        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                if vertex == end:
                    return True
                visited.add(vertex)
                stack.extend(neighbor for neighbor in self.graph.get(vertex, []) if neighbor not in visited)
        
        return False

    def bfs(self, source, target):
        if source not in self.graph or target not in self.graph:
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
                if node in self.graph:
                    for neighbor in self.graph[node]:
                        if neighbor not in visited:
                            fila.put((neighbor, path + [neighbor]))
        return None

    def get_graph_shortest_path(self, source, target):
        return self.bfs(source, target)
  
    def get_nodes(self, search_type):
        try:
            while True:
                with open("data/pt-wiki-pages-final.txt", 'r') as file:
                    lines = file.readlines()

                nodes = [line.strip() for line in random.sample(lines, 2)]
                if search_type == 'bfs':
                    if self.bfs(nodes[0], nodes[1]):
                        return nodes
                else: 
                    if self.dfs(nodes[0], nodes[1]):
                        return nodes

        except FileNotFoundError:
            return None
