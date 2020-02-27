__author__ = "GODEFROY"
__filename__ = "reddit_hyperlink.py"
__date__ = "27/02/20"

from graph import DirectedGraph

def read_file(file_name):
    subreddit_file = open(file_name)
    subreddit_links_list = subreddit_file.readlines()[1:]
    subreddit_file.close()

    for i in range(0, len(subreddit_links_list)):
        split = subreddit_links_list[i].split('\t')
        split = (split[0], split[1])
        subreddit_links_list[i] = split
    return subreddit_links_list


def create_graph_from_edges(links_list):
    graph = DirectedGraph()
    for sub1, sub2 in set(links_list):
        if sub1 not in graph.edges:
            graph.add_vertex(sub1)
        if sub2 not in graph.edges:
            graph.add_vertex(sub2)
        graph.add_edge(sub1, sub2, 1)
    return graph


def create_graph(file_name):
    # Creates graph with no duplicate edge
    return create_graph_from_edges(set(read_file(file_name)))


def classement_deg(graph):
    deg = dict()
    for node in graph:
        deg[node] = len(graph[node])
    return  deg

x = create_graph('soc-redditHyperlinks-title.tsv')


def max_deg(graph, n):
    m = 0
    classement = []
    degre = sorted(classement_deg(graph).items() , key = lambda item : item[1], reverse = True)
    for node in degre:
        classement += [node]
        m += 1
        if m >= n:
            break
    return classement


def nb_nuldeg(graph):
    compteur = 0
    degre = sorted(classement_deg(graph).items() , key = lambda item : item[1])
    for node in degre:
        if node[1] != 0:
            break
        compteur += 1
    return compteur



def part_total(graph, pourcentage):
    m = 0
    classement = []
    degre = sorted(classement_deg(graph).items(), key=lambda item: item[1], reverse=True)
    nbsub = pourcentage * len(degre) /100
    part = 0
    parttot = 0
    for node in degre:
        if m <= nbsub:
            part += node[1]
            parttot += node[1]
        else:
            parttot += node[1]
        m +=1
    return part/parttot * 100

print(x.shortest_way_node('disney','vegan'))
print(x.shortest_way_node('greenbaypackers','missouripolitics'))







