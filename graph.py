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
        if start == end:
            False

        visited = set()
        stack = [start]
        
        while stack:
            node = stack.pop()
            if node not in visited:
                if node == end:
                    return True
                visited.add(node)
                stack.extend(neighbor for neighbor in self.graph.get(node, []) if neighbor not in visited)
        
        return False

    def bfs(self, source, target):
        if source not in self.graph or target not in self.graph:
            return None

        if source == target:
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
  
    def get_nodes(self, search_type):
        try:
            with open("data/pt-wiki-pages-final.txt", 'r') as file:
                lines = file.readlines()

            while True:
                nodes = [line.strip() for line in random.sample(lines, 2)]
                source = nodes[0]
                target = nodes[1]

                if source == target:
                    continue

                if source in self.graph and target in self.graph:
                    if search_type == 'bfs':
                        result = self.bfs(source, target)
                    else:
                        result = self.dfs(source, target)
                    
                    if result is not None or result == True:
                        return nodes
            

        except FileNotFoundError:
            return None
