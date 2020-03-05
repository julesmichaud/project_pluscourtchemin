__author__ = "GODEFROY"
__filename__ = "reddit_hyperlink.py"
__date__ = "27/02/20"

from graph import *


def read_file(file_name):
    """Create edges for a graph"""
    subreddit_file = open(file_name)
    subreddit_links_list = subreddit_file.readlines()[1:]
    subreddit_file.close()

    for i in range(0, len(subreddit_links_list)):
        split = subreddit_links_list[i].split('\t')
        split = (split[0], split[1])
        subreddit_links_list[i] = split
    return subreddit_links_list


def create_graph_from_edges(links_list):
    """Create graph with the edges list"""
    graph = DirectedGraph()
    for sub1, sub2 in set(links_list):
        if sub1 not in graph.edges:
            graph.add_vertex(sub1)
        if sub2 not in graph.edges:
            graph.add_vertex(sub2)
        graph.add_edge(sub1, sub2, 1)
    return graph


def create_graph(file_name):
    """Creates graph with no duplicate edge"""
    return create_graph_from_edges(set(read_file(file_name)))


def ranking_degree(graph):
    """Create dictionaries with the nodes degree"""
    deg = dict()
    for node in graph:
        deg[node] = len(graph[node])
    return deg


def max_deg(graph, n):
    """Return the n nodes with the maximum degree"""
    m = 0
    ranking = []
    degree = sorted(ranking_degree(graph).items(), key=lambda item: item[1], reverse=True)
    for node in degree:
        ranking += [node]
        m += 1
        if m >= n:
            break
    return ranking


def nb_nul_deg(graph):
    """Return the nodes with no link between other communities"""
    counter = 0
    degree = sorted(ranking_degree(graph).items(), key=lambda item: item[1])
    for node in degree:
        if node[1] != 0:
            break
        counter += 1
    return counter


def part_total(graph, percentage):
    """Total interactions part of the "percentage" more active percents communities"""
    m = 0
    degree = sorted(ranking_degree(graph).items(), key=lambda item: item[1], reverse=True)
    nb_sub = percentage * len(degree) / 100
    part = 0
    part_tot = 0
    for node in degree:
        if m <= nb_sub:
            part += node[1]
            part_tot += node[1]
        else:
            part_tot += node[1]
        m += 1
    return part / part_tot * 100


T = time()
x = create_graph('soc-redditHyperlinks-title.tsv')
T = time() - T
print("-> Time to load a graph :", T)
'''Take 2.1s'''

print("\nTOP TEN SUBREEDDITS\n")
T = time()
print(max_deg(x, 10))
T = time() - T
print("-> Time to calculate top ten subbredits :", T)
'''Take 0.09s'''

print("\nNON LINKED SUBREDDITS NUMBER\n")
T = time()
print(nb_nul_deg(x))
T = time() - T
print("-> Time to calculate non linked subbredits number :", T)
'''Take 0.09s'''

print("\nTOTAL INTERACTION PART OF THE TWO MORE ACTIVE PERCENTS COMMUNITIES")
T = time()
print(part_total(x, 2))
T = time() - T
print("-> Time to calculate the total interaction part of the two more active percents communities :", T)
'''Take 0.1s'''

print("\nSHORTEST WAY BETWEEN 'disney' AND 'vegan'\n")
T = time()
print(x.shortest_way_node('disney', 'vegan'))
T = time() - T
print("-> Time to calculate the shortest way between 'disney' and 'vegan' :", T)
'''Take 43s'''

print("\nSHORTEST WAY BETWEEN 'greenbaypackers' AND 'missouripolitics'\n")
T = time()
print(x.shortest_way_node('greenbaypackers', 'missouripolitics'))
T = time() - T
print("-> Time to calculate the shortest way between 'greenbaypackers' and 'missouripolitics' :", T)
'''Take 711s'''
