__author__ = 'julesmichaud'
__filename__ = 'teste_graph_generation.py'
__date__ = '20/02/20'

from graph_generation import *

# Undirected tests

G1 = generate_random_graph(10, 10)
G2 = generate_random_graph(10, 45)
G3 = generate_random_graph(0, 0)
G4 = generate_random_graph(0, 10)
G5 = generate_random_graph(10, 46)


print("\n Undirected tests \n")
print(G1, "\n")
print(G2, "\n")
print(G3, "\n")
print(G4, "\n")
print(G5, "\n")

# Directed tests

G1 = generate_random_graph(10, 10, True)
G2 = generate_random_graph(10, 90, True)
G3 = generate_random_graph(0, 0, True)
G4 = generate_random_graph(0, 10, True)
G5 = generate_random_graph(10, 91, True)


print("\n Directed tests \n")
print(G1, "\n")
print(G2, "\n")
print(G3, "\n")
print(G4, "\n")
print(G5, "\n")

# Communities tests

G1 = generate_random_community_graph([2, 1], 0, 0)
G2 = generate_random_community_graph([2, 1], 1, 0)
G3 = generate_random_community_graph([2, 1], 0, 1)
G4 = generate_random_community_graph([2, 1], 1, 1)
G5 = generate_random_community_graph([2, 1], 0.5, 0.5)


print("\n Communities tests \n")
print(G1, "\n")
print(G2, "\n")
print(G3, "\n")
print(G4, "\n")
print(G5, "\n")
