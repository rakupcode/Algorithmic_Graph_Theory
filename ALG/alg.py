class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = {i: [] for i in range(vertices)}

    def add_edge(self, u, v, weight=1):
        self.graph[u].append((v, weight))
        if self.is_undirected:
            self.graph[v].append((u, weight))

    def print_graph(self):
        for i in range(self.vertices):
            print(f"Vertex {i}:", end="")
            for j in self.graph[i]:
                print(f" -> {j}", end="")
            print()

class UndirectedUnweightedGraph(Graph):
    def __init__(self, vertices):
        super().__init__(vertices)
        self.is_undirected = True

class UndirectedWeightedGraph(Graph):
    def __init__(self, vertices):
        super().__init__(vertices)
        self.is_undirected = True

class DirectedUnweightedGraph(Graph):
    def __init__(self, vertices):
        super().__init__(vertices)
        self.is_undirected = False

class DirectedWeightedGraph(Graph):
    def __init__(self, vertices):
        super().__init__(vertices)
        self.is_undirected = False
