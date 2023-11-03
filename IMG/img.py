class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = []
        self.matrix = []

    def add_edge(self, u, v, weight=1):
        edge_index = len(self.edges)
        self.edges.append((u, v))
        for _ in range(len(self.matrix)):
            self.matrix[_].append(0)
        self.matrix[u][edge_index] = weight
        if self.is_undirected:
            self.matrix[v][edge_index] = weight
        else:
            self.matrix[v][edge_index] = -weight

    def print_graph(self):
        for i in range(self.vertices):
            for j in range(len(self.edges)):
                print(self.matrix[i][j], end=' ')
            print()

class UndirectedUnweightedGraph(Graph):
    def __init__(self, vertices):
        super().__init__(vertices)
        self.is_undirected = True
        self.matrix = [[0 for _ in range(vertices)] for _ in range(vertices)]

class UndirectedWeightedGraph(Graph):
    def __init__(self, vertices):
        super().__init__(vertices)
        self.is_undirected = True
        self.matrix = [[0 for _ in range(vertices)] for _ in range(vertices)]

class DirectedUnweightedGraph(Graph):
    def __init__(self, vertices):
        super().__init__(vertices)
        self.is_undirected = False
        self.matrix = [[0 for _ in range(vertices)] for _ in range(vertices)]

class DirectedWeightedGraph(Graph):
    def __init__(self, vertices):
        super().__init__(vertices)
        self.is_undirected = False
        self.matrix = [[0 for _ in range(vertices)] for _ in range(vertices)]
