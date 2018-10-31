from collections import defaultdict

class Graph:
    def __init__(self,vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self,u,v,w):
        self.graph[u].append((v,w))

    def TopologicalSort(self):
        linear_order = []
        in_degree = [0]*self.V
        next = []

        for i in range(self.V):
            for node,weight in self.graph[i]:
                in_degree[node] += 1
        for i in range(self.V):
            if in_degree[i] == 0:
                next.append(i)

        while next:
            vertex_u = next.pop(0)
            linear_order.append(vertex_u)
            for node,weight in self.graph[vertex_u]:
                in_degree[node] -= 1
                if in_degree[node] == 0:
                    next.append(node)
        return linear_order



    def DAG_SHORTEST_PATHS(self,s):

        l = self.TopologicalSort()
        Shortest = [float('Inf')]*self.V
        Shortest[s] = 0
        pred =[0]*self.V

        for vertex_u in l:
            for node,weight in self.graph[vertex_u]:
                if Shortest[vertex_u] + weight < Shortest[node]:
                    Shortest[node] = Shortest[vertex_u] + weight
                    pred[node] = vertex_u

        for i in range(self.V):
            if Shortest[i] != float('Inf'):
                print(Shortest[i])
            else:
                print('Inf')

g = Graph(6)
g.addEdge(0, 1, 5)
g.addEdge(0, 2, 3)
g.addEdge(1, 3, 6)
g.addEdge(1, 2, 2)
g.addEdge(2, 4, 4)
g.addEdge(2, 5, 2)
g.addEdge(2, 3, 7)
g.addEdge(3, 4, -1)
g.addEdge(4, 5, -2)

s = 1

print ("Following are the shortest distances from source %d " % s)
g.DAG_SHORTEST_PATHS(s)





