__author__ = 'julesmichaud'
__filename__ = 'graph.py.py'
__date__ = '19/02/20'

from copy import deepcopy


class DirectedGraph:

    def __init__(self, edges):
        self.edges = edges

    @classmethod
    def empty_graph(cls):
        return cls({})

    @property
    def vertices(self):
        v = set()
        for node in self:
            v.add(node)
        return v

    @property
    def edges(self):
        return self.__edges

    @edges.setter
    def edges(self, x):
        """verification edges is a dictionary of dictionaries"""
        if x == {} or (type(x) == dict and (type(y) == dict for y in x.val)):
            self.__edges = x

    def remove_vertex(self, vertex):
        for node in self:
            '''delete the node if it's existing as a key or just pass to the next one if it doesn't'''
            try:
                del node[vertex]
            except KeyError:
                pass
        del self.edges[vertex]

    def add_vertex(self, vertex):
        self.edges[vertex] = {}

    def add_edge(self, vertex1, vertex2, weight):
        if vertex1 not in self.edges:
            self.add_vertex(vertex1)
        if vertex2 not in self.edges:
            self.add_vertex(vertex2)
        self.edges[vertex1][vertex2] = weight

    def remove_edge(self, vertex1, vertex2):
        """delete the edge if it's existing or just pass if it doesn't"""
        try:
            del self.edges[vertex1][vertex2]
        except KeyError:
            pass

    def set_weight(self, vertex1, vertex2, weight):
        self.edges[vertex1][vertex2] = weight

    def reset(self):
        self.edges = {}

    def sous_graph(self, v):
        """we determine the non-wished nodes and we delete them correctly thanks to remove_vertex"""
        graph = deepcopy(self)
        nodes = graph.vertices.difference(v)
        graph.remove_vertex(node for node in nodes)
        return graph

    def __len__(self):
        return len(self.edges)

    def __getitem__(self, item):
        return self.edges[item]

    def __iter__(self):
        for key in self.edges:
            yield key

    def __str__(self):
        """print the set of the vertex and the edges list with their weight"""
        vertex = set()
        ed = []
        for key in self:
            vertex.add(key)
            for i in self[key]:
                ed.append(["Edge :", (key, i), "Weight :", self[key][i]])
        return "S = " + str(vertex) + "\n" + "E = " + str(ed)


class UndirectedGraph(DirectedGraph):

    def __init__(self, edges):
        super().__init__(edges)

    def remove_vertex(self, vertex):
        """an undirected graph permit us to code remove_vertex with a better complexity than a directed graph"""
        for node in self[vertex]:
            del self[node][vertex]
        del self.edges[vertex]

    def add_edge(self, vertex1, vertex2, weight):
        if vertex1 not in self.edges:
            self.add_vertex(vertex1)
        if vertex2 not in self.edges:
            self.add_vertex(vertex2)
        self.edges[vertex1][vertex2] = weight
        self.edges[vertex2][vertex1] = weight

    def remove_edge(self, vertex1, vertex2):
        try:
            del self.edges[vertex1][vertex2]
            del self.edges[vertex2][vertex1]
        except KeyError:
            pass

    def set_weight(self, vertex1, vertex2, weight):
        self.edges[vertex1][vertex2] = weight
        self.edges[vertex2][vertex1] = weight
