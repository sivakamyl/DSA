class Graph:
    # using adjacency list
    def __init__(self):
        # graph is created with hash table with key as vertex and value denoted the list of vertices the key is connected to.
        self.graph = {}
        self.directed = False

    def addVertex(self, vertex):
        # if vertex is not already present, initialise it with no edges
        if vertex not in self.graph:
            self.graph[vertex] = []
    
    def addEdge(self, src, dest):
        # Add src and dest vertices to graph if not already present
        self.addVertex(src)
        self.addVertex(dest)

        # add the destionation vertex to the list of vertices that form an edge with src
        self.graph[src].append(dest)

        # if graph is undirected, add birectional edge
        if not self.directed:
            self.graph[dest].append(src)

    def displayGraph(self):
        for vertex in self.graph:
            print (f"{vertex} -> {self.graph[vertex]}")

    def bfs(self, startVertex):
        queue = [startVertex]
        visited = { startVertex: True }

        while queue:
            currentVertex = queue.pop(0)
            print (currentVertex, end = ' ')

            for neighbour in self.graph[currentVertex]:
                if neighbour not in visited:
                    queue.append(neighbour)
                    visited[neighbour] = True
        return

    def dfs(self, vertex, visited):
        if vertex not in visited:
            print (vertex, end = ' ')
            visited[vertex] = True
            for neighbour in self.graph[vertex]:
                self.dfs(neighbour, visited)



# Create the graph
G = Graph()
G.addEdge('A', 'B')
G.addEdge('C','A')
G.addEdge('B', 'C')
G.addEdge('C','D')
G.addEdge('A', 'E')
G.addEdge('D','A')

# Display the graph
G.displayGraph()
G.dfs('A',{})