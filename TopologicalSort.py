from collections import defaultdict

class Graph:

    def __init__(self,vertices):
        self.graph = defaultdict(list)
        self.Vertex = vertices

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def Topological_Sort(self):
        linear_order = []
        in_degree = [0]*self.Vertex
        next = []

        for i in range(self.Vertex):
            for j in self.graph[i]:
                in_degree[j] += 1

        for l in range(self.Vertex):
            if in_degree[l] == 0:
                next.append(l)

        while next:
            vertex_u = next.pop(0)
            linear_order.insert(len(linear_order),vertex_u)

            for v in self.graph[vertex_u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    next.append(v)

        return linear_order

g= Graph(6)
g.addEdge(5, 2);
g.addEdge(5, 0);
g.addEdge(4, 0);
g.addEdge(4, 1);
g.addEdge(2, 3);
g.addEdge(3, 1);

print(g.Topological_Sort())



