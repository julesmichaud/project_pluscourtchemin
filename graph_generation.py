__author__ = 'julesmichaud'
__filename__ = 'graph_generation.py'
__date__ = '20/02/20'

from graph import *
import random


def generate_random_graph(n_nodes, n_edges, directed=False):
    if n_nodes == 0 and n_edges == 0:
        if not directed:
            return UndirectedGraph.empty_graph()
        else:
            return DirectedGraph.empty_graph()
    elif n_nodes > n_edges or (n_edges > (n_nodes * (n_nodes - 1) / 2) and not directed) or (
            n_edges > (n_nodes * (n_nodes - 1)) and directed):
        return ValueError
    elif not directed:
        non_used_nodes = [i for i in range(1, n_nodes)]
        used_nodes = [0]
        counter = 0
        graph = UndirectedGraph.empty_graph()
        for i in range(n_nodes):
            graph.edges[i] = {}
        while len(non_used_nodes) != 0:
            s1 = random.choice(non_used_nodes)
            s2 = random.choice(used_nodes)
            non_used_nodes.remove(s1)
            used_nodes.append(s1)
            graph.edges[s1][s2] = 1
            graph.edges[s2][s1] = 1
            counter += 1
        while counter != n_edges:
            s1 = random.choice(used_nodes)
            s2 = random.choice(used_nodes)
            if (s1 != s2) and (s2 not in graph.edges[s1].keys()):
                graph.edges[s1][s2] = 1
                graph.edges[s2][s1] = 1
                counter += 1
    else:
        graph = DirectedGraph.empty_graph()
        counter = 0
        for i in range(n_nodes):
            graph.edges[i] = {}
        while counter != n_edges:
            s1 = random.randint(0, n_nodes - 1)
            s2 = random.randint(0, n_nodes - 1)
            if (s1 != s2) and (s2 not in graph.edges[s1].keys()):
                graph.edges[s1][s2] = 1
                counter += 1
    return graph


def generate_random_community_graph(n_nodes_per_community, p_intra, p_inter):
    graph = UndirectedGraph.empty_graph()
    for community in range(len(n_nodes_per_community)):
        for node in range(n_nodes_per_community[community]):
            graph.edges[(community, node)] = {}
    for s1 in graph.edges.keys():
        for s2 in graph.edges.keys():
            if (s1 != s2) and (s2 not in graph.edges[s1].keys()):
                p = random.random()
                if s1[0] == s2[0]:
                    if p < p_intra:
                        graph.edges[s1][s2] = 1
                        graph.edges[s2][s1] = 1
                else:
                    if p < p_inter:
                        graph.edges[s1][s2] = 1
                        graph.edges[s2][s1] = 1
    return graph
