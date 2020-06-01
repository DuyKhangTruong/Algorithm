from collections import defaultdict
import math
class Graph:
    def __init__(self,vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def addEdge(self,u,v,w):
        self.graph[u] = (v,w)


    def ShortestPath(self,S):
        shortest = [float('inf')]*self.V
        pred = [None]*self.V
        shortest[S] = 0

        Q = []
        for i in self.V:
            for j in self.graph[i]:
                Q.append(j)

        while Q:
            u = Q.remove(shortest.index(min(shortest)))
            for vertex, weigh in self.graph[u]:
                if shortest[u] + weigh < shortest[vertex]:
                    shortest[vertex] = shortest[u] + weigh
                    pred[vertex] = u



