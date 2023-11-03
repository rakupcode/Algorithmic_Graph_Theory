class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.matrix = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def add_edge(self, u, v, weight=1):
        self.matrix[u][v] = weight
        if self.is_undirected:
            self.matrix[v][u] = weight

    def print_graph(self):
        for i in range(self.vertices):
            for j in range(self.vertices):
                print(self.matrix[i][j], end=' ')
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
