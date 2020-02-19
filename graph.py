__author__ = 'julesmichaud'
__filename__ = 'graph.py.py'
__date__ = '19/02/20'

from copy import deepcopy


class DirectedGraph:

    def __init__(self, edges={}):
        self.edges = edges

    def getVertices(self):
        V = set()
        for sommet in self :
            V.add(sommet)
        return V

    @property
    def vertices(self):
        return self.getVertices()

    @property
    def edges(self):
        return self.__edges

    @edges.setter
    def edges(self, x):
        if x == {} or (type(x) == dict and (type(y) == dict for y in x.val)):
            self.__edges = x

    def remove_vertex(self, vertex):
        for sommet in self:
            try:
                del sommet[vertex]
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
        try:
            del self.edges[vertex1][vertex2]
        except KeyError:
            pass

    def setWeight(self, vertex1, vertex2, weight):
        self.edges[vertex1][vertex2] = weight

    def reset(self):
        self.edges = {}

    def sous_graphe(self, V2):
        G = deepcopy(self)
        sommets = G.vertices.difference(V2)
        G.remove_vertex(sommet for sommet in sommets)
        return G

    def __len__(self):
        compte = 0
        for vertex in self:
            compte += 1
        return compte

    def __getitem__(self, item):
        return self.edges[item]

    def __iter__(self):
        for key in self.edges:
            yield key

    def __str__(self):
        vertex = set()
        ed = []
        for key in self:
            vertex.add(key)
            for i in self[key]:
                ed.append([key, i])
        return 'S = ' + str(vertex) + '       ' + 'E = ' + str(ed)

