__author__ = 'julesmichaud'
__filename__ = 'test_graph.py'
__date__ = '19/02/20'

from graph import *

graph = DirectedGraph()
graph.add_vertex(1)
graph.add_edge(1, 2, 3)
graph.add_edge(2, 1, 1)
graph.add_edge(2, 3, 1)

print(graph.vertices)  # affiche dict_keys([1,2,3])
print(len(graph))  # affiche 3
print(graph[2])  # affiche {1: 1, 3:1}
print(graph)

for vertex in graph:
    print(vertex)

graph.remove_edge(1, 2)
print(graph)
