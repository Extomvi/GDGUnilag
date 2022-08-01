"""
Dfs implementation
"""
from collections import defaultdict

class DFS:

    def __init__(self):
        self.graph = defaultdict(list)

    def addItem(self, u, v):
        self.graph[u].append(v)

    def dfsUtil(self, v, visited):
        visited[v] = True
        print(v)

        for i in self.graph[v]:
            if visited[i] == False:
                self.dfsUtil(i, visited)

    def DFS(self):
        V = len(self.graph)

        visited = [False]*(V)

        for i in range(V):
            if visited[i] == False:
                self.dfsUtil(i, visited)

g = DFS()
g.addItem(0,1)
g.addItem(0,2)
g.addItem(1,2)
g.addItem(2,0)
g.addItem(2,3)
g.addItem(3,3)
print("Here is the DFS :")
g.DFS()
