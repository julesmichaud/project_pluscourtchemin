__author__ = 'julesmichaud'
__filename__ = 'teste_graph.py'
__date__ = '19/02/20'

from graph import *

# Class basic tests

print("\nCLASS BASIC TESTS\n")

graph = UndirectedGraph.empty_graph()
graph.add_vertex(1)
graph.add_edge(1, 2, 3)
graph.add_edge(2, 1, 1)
graph.add_edge(2, 3, 1)

print(graph.vertices)  # print dict_keys([1, 2, 3])
print(len(graph))  # print 3
print(graph[2])  # print {1: 1, 3: 1}
print("\n")

print(graph)
print("\n")

for vertex in graph:
    print(vertex)
print("\n")

graph.remove_edge(1, 2)
print(graph)
print("\n")

# Shortest way tests

print("\nSHORTEST WAY TESTS\n")

graph_2 = UndirectedGraph.empty_graph()

graph_2.add_edge(0, 1, 1)
graph_2.add_edge(0, 2, 2)
graph_2.add_edge(0, 3, 10)
graph.add_edge(0, 4, 8)
graph_2.add_edge(0, 5, 3)
graph_2.add_edge(1, 2, 2)
graph_2.add_edge(2, 3, 8)
graph_2.add_edge(3, 4, 1)
graph_2.add_edge(4, 5, 1)

graph_3 = DirectedGraph.empty_graph()

graph_3.add_edge(1, 2, 3)
graph_3.add_edge(1, 3, 1)
graph_3.add_edge(3, 2, 1)
graph_3.add_edge(3, 4, 1)
graph_3.add_edge(4, 1, 1)


print(graph_2.shortest_way(
    0))  # print {0: [0,"0"], 1: [1, "0-1"], 2: [2, "0-2"], 3: [5, "0-5-4-3"], 4: [4, "0-5-4"], 5: [3, "0-5"]}
print(graph_2.bellman_ford(0))  # print {0: 0, 1: 1, 2: 2, 3: 5, 4: 4, 5: 3}
print(graph_2.dijkstra(0))  # print {0: 0, 1: 1, 2: 2, 3: 5, 4: 4, 5: 3}
print("\n")

graph_2.remove_edge(0, 1)

print(graph_2.shortest_way(
    0))  # print {0: [0,"0"], 1: [4, "0-1-2"], 2: [2, "0-2"], 3: [5, "0-5-4-3"], 4: [4, "0-5-4"], 5: [3, "0-5"]}
print(graph_2.bellman_ford(0))  # print {0: 0, 1: 4, 2: 2, 3: 5, 4: 4, 5: 3}
print(graph_2.dijkstra(0))  # print {0: 0, 1: 4, 2: 2, 3: 5, 4: 4, 5: 3}
print("\n")

graph_2.remove_edge(1, 2)

print(graph_2.shortest_way(
    0))  # print {0: [0,"0"], 1: [inf, ""], 2: [2, "0-2"], 3: [5, "0-5-4-3"], 4: [4, "0-5-4"], 5: [3, "0-5"]}
print(graph_2.bellman_ford(0))  # print {0: 0, 1: inf, 2: 2, 3: 5, 4: 4, 5: 3}
print(graph_2.dijkstra(0))  # print {0: 0, 1: inf, 2: 2, 3: 5, 4: 4, 5: 3}
print("\n")

print(graph_3.shortest_way(1))  # print {1: [0, '1'], 2: [2, '1-3-2'], 3: [1, '1-3'], 4: [2, '1-3-4']}
print(graph_3.bellman_ford(1))  # print {1: 0, 2: 2, 3: 1, 4: 2}
print(graph_3.dijkstra(1))  # print {1: 0, 2: 2, 3: 1, 4: 2}
print("\n")

# Shortest way node tests

print("\nSHORTEST WAY NODE TESTS\n")

print(graph_2.shortest_way_node(0, 0))  # print [0,"0"]
print(graph_2.shortest_way_node(0, 1))  # print [inf, ""]
print(graph_2.shortest_way_node(0, 2))  # print [2, "0-2"]
print(graph_2.shortest_way_node(0, 3))  # print [5, "0-5-4-3"]
print(graph_2.shortest_way_node(0, 4))  # print [4, "0-5-4"]
print(graph_2.shortest_way_node(0, 5))  # print [3, "0-5"]
print("\n")
