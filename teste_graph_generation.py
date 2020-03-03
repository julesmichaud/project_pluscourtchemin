__author__ = 'julesmichaud'
__filename__ = 'teste_graph_generation.py'
__date__ = '20/02/20'

from graph_generation import *

# Undirected tests

print("\nUNDIRECTED TESTS\n")

G1 = generate_random_graph(10, 10)
G2 = generate_random_graph(10, 45)
G3 = generate_random_graph(0, 0)
G4 = generate_random_graph(0, 10)
G5 = generate_random_graph(10, 46)


print(G1, "\n")    # print a connected graph
print(G2, "\n")    # print a connected complete graph
print(G3, "\n")    # print an empty graph
print(G4, "\n")    # print an error
print(G5, "\n")    # print an error

# Directed tests

print("\nDIRECTED TESTS\n")

G1 = generate_random_graph(10, 5, True)
G2 = generate_random_graph(10, 90, True)
G3 = generate_random_graph(0, 0, True)
G4 = generate_random_graph(0, 10, True)
G5 = generate_random_graph(10, 91, True)


print(G1, "\n")    # print a connected graph
print(G2, "\n")    # print a connected complete graph
print(G3, "\n")    # print an empty graph
print(G4, "\n")    # print an error
print(G5, "\n")    # print an error

# Communities tests

print("\nCOMMUNITIES TESTS\n")

G1 = generate_random_community_graph([2, 1], 0, 0)
G2 = generate_random_community_graph([2, 1], 1, 0)
G3 = generate_random_community_graph([2, 1], 0, 1)
G4 = generate_random_community_graph([2, 1], 1, 1)
G5 = generate_random_community_graph([2, 1], 0.5, 0.5)


print(G1, "\n")    # print an empty graph
print(G2, "\n")    # print an intra-community graph
print(G3, "\n")    # print an inter-communities graph
print(G4, "\n")    # print an connected graph
print(G5, "\n")
