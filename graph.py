__author__ = 'julesmichaud'
__filename__ = 'graph.py.py'
__date__ = '19/02/20'

from copy import deepcopy
import random
from time import *
import heapq
# import networkx as nx


class DirectedGraph:

    def __init__(self, edges={}):
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

    def dijkstra(self, node):
        """return a dictionary of lists with the length of the shortest way, and the shortest way nodes for each node"""
        used_nodes = set()
        way = dict()
        '''initialisation'''
        for i in self.vertices:
            way[i] = float('inf')
        way[node] = 0
        '''calculation of the shortest ways as long as there are nodes we didn't find the shortest way'''
        while len(self.vertices.difference(used_nodes)) != 0:
            mini = float("inf")
            arg_mini = None
            for x in self.vertices.difference(used_nodes):
                if way[x] <= mini:
                    mini = way[x]
                    arg_mini = x
            used_nodes.add(arg_mini)
            non_used_neighbours = set(self.edges[arg_mini].keys()).difference(used_nodes)
            '''calculation of the new possible ways between x and his neighbours not yet used'''
            for neighbour in non_used_neighbours:
                way[neighbour] = min(way[neighbour], mini + self.edges[arg_mini][neighbour])
        return way

    def shortest_way(self, node):
        """return a dictionary of lists with the length of the shortest way, and the shortest way nodes for each node"""
        used_nodes = set()
        queue = []
        way = dict()
        '''initialisation'''
        for i in self.vertices:
            heapq.heappush(queue, (float('inf'), i, ""))
        heapq.heappush(queue, (0, node, str(node)))
        '''calculation of the shortest ways as long as there are nodes we didn't find the shortest way'''
        while len(self.vertices.difference(used_nodes)) != 0:
            x = heapq.heappop(queue)
            '''check that x has not yet a shortest way'''
            if x[1] not in used_nodes:
                way[x[1]] = [x[0], x[2]]
                used_nodes.add(x[1])
                non_used_neighbours = set(self.edges[x[1]].keys()).difference(used_nodes)
                '''calculation of the new possible ways between x and his neighbours not yet used'''
                for neighbour in non_used_neighbours:
                    heapq.heappush(queue,
                                   (x[0] + self.edges[x[1]][neighbour], neighbour, str(x[2]) + "-" + str(neighbour)))
        return way

    def shortest_way_node(self, node_1, node_2):
        """calculation of all the shortest ways until finding the shortest way into node_1 and node_2"""
        used_nodes = set()
        queue = []
        way = dict()
        '''initialisation'''
        for i in self.vertices:
            heapq.heappush(queue, (float('inf'), i, ""))
        heapq.heappush(queue, (0, node_1, str(node_1)))
        x = heapq.heappop(queue)
        '''calculation of the shortest ways as long as we didn't find the node_2 one'''
        while x[1] != node_2 and len(self.vertices.difference(used_nodes)) != 0:
            '''check that x has not yet a shortest way'''
            if x[1] not in used_nodes:
                way[x[1]] = [x[0], x[2]]
                used_nodes.add(x[1])
                non_used_neighbours = set(self.edges[x[1]].keys()).difference(used_nodes)
                '''calculation of the new possible ways between x and his neighbours not yet used'''
                for neighbour in non_used_neighbours:
                    heapq.heappush(queue,
                                   (x[0] + self.edges[x[1]][neighbour], neighbour, str(x[2]) + "-" + str(neighbour)))
            x = heapq.heappop(queue)
        return [x[0], x[2]]

    def bellman_ford(self, node):
        """calculation of the shortest way thanks of dynamic programming"""
        opt = dict()
        '''initialisation'''
        for i in self.vertices:
            opt[i] = float("inf")
        opt[node] = 0
        '''for each iteration, we calculate the shortest way between "node" and the other nodes with at maximum k
        edges'''
        for k in range(1, len(self.vertices)-1):
            for node_1 in self.vertices:
                for node_2 in self.edges[node_1]:
                    opt[node_2] = min(opt[node_2], opt[node_1] + self.edges[node_1][node_2])
        '''return the shortest way for each node with at maximum len(self.vertices)-1 edges, that's exactly the shortest
        way for each node'''
        return opt

    def to_networkx(self):
        return nx.Graph(self.edges, create_using=nx.DiGraph)


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
