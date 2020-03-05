__author__ = "GODEFROY"
__filename__ = "temps_networkx.py"
__date__ = "27/02/20"

from graph import *
from graph_generation import *
from time import *
import matplotlib.pyplot as plt

liste_graph = []
nb_node = [1,2,3,4,5,6,7,8,9,10,11]
for i in nb_node:
    graph = generate_random_graph(i*10**3, 0,7*(i*10**3)**2)
    liste_graph.append(graph)

#Dijkstra

#times =[]
#for graphs in liste_graph:
#    debut = time()
#    dijk = graphs.dijkstra(0)
#    fin = time()
#    times.append(fin - debut)
times_dij = [0.2579963207244873, 1.0236315727233887, 2.293308734893799, 3.9620697498321533, 6.1064772605896, 9.428546667098999, 12.60987377166748, 16.256490468978882, 20.485872507095337, 25.46430230140686,30.78547477722168]

plt.figure(1)
plt.ylabel('Temps (s)',fontsize = 20)
plt.xlabel('Nombre de noeud $n$', fontsize = 20)
plt.title(r"Nombre d'arrete = $0.7n^2$" )

plt.plot(nb_node,times_dij, label = 'Dijkstra')


#Shortest_way


#times_short =[]
#for graphs in liste_graph:
#   debut = time()
#   dijk = graphs.shortest_way(0)
#   fin = time()
#   times_short.append(fin - debut)

times_short =[0.11876630783081055, 0.4582517147064209, 1.0067143440246582, 1.7419414520263672, 2.6944236755371094, 4.1708643436431885, 5.588544130325317, 7.295061826705933, 9.1475670337677, 11.172382831573486, 13.879867315292358]

plt.plot(nb_node,times_short, label = "Shortest_way")




#bellman_ford

#times_bellman =[]
#for graphs in liste_graph:
#   debut = time()
#   dijk = graphs.bellman_ford(0)
#   fin = time()
#   times_bellman.append(fin - debut)

times_bellman =[0.2663583755493164, 1.0406832695007324, 2.42586088180542, 4.2683329582214355, 6.7486772537231445, 9.617671728134155, 13.152548551559448, 17.207563638687134, 21.523457288742065, 26.825584411621094, 32.797017335891724]

plt.plot(nb_node,times_bellman, label = "Bellman_ford")
plt.legend(loc = 'best')

plt.show()





