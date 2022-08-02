"""
Recursive traversal implementation of depth first search algorithm
"""
#Recursive traversal method
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E'],
    'C': ['D', 'E'],
    'D': [],
    'E': []
}

visited = set()

def dfs(visited, graph, root):
    if root not in visited:
        print(root)
        visited.add(root)
        for next in graph[root]:
            dfs(visited, graph, next) #recursive call
dfs(visited, graph, 'A')
