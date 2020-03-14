__filename__ = "graph_temps.py"
__date__ = "27/02/20"

from graph_generation import *


def first_generation_list_graph(nb_test, coeff):
    """Creation of a graphs list for 4.1 in order to make some time tests"""
    list_graph = []
    for j in range(1, nb_test + 1):
        nb_nodes = j * 10 ** 3
        start = time()
        graph = generate_random_graph(nb_nodes, int(coeff * nb_nodes ** 2))
        end = time()
        list_graph.append(graph)
        print("Graph " + str(j) + " on " + str(nb_test) + " created, in " + str(end - start) + " s")
    return list_graph


def second_generation_list_graph(nb_test, fixed_node):
    """Creation of a graphs list for 4.2 in order to make some time tests"""
    list_graph = []
    for j in range(nb_test):
        start = time()
        graph = generate_random_graph(fixed_node,
                                      int((1 / fixed_node + (0.4 - 1 / fixed_node) * j / (
                                                  nb_test - 1)) * fixed_node ** 2))
        end = time()
        list_graph.append(graph)
        print("Graph " + str(j + 1) + " on " + str(nb_test) + " created, in " + str(end - start) + " s")
    return list_graph


def first_time_test(nb_test, coeff, condition, condition_bellman=False):
    """Calculation of the 4.1 times if condition is True or just return the times already calculated else"""
    if condition:
        """Question 4.1"""
        list_graph = first_generation_list_graph(nb_test, coeff)
        print("list_graph calculated !\n")
        time_dijkstra = []
        time_shortest_way = []
        time_bellman_ford = []
        time_min = []
        time_max = []
        time_mean = []
        time_median = []
        for i in range(nb_test):
            graphs = list_graph[i]
            '''Time calculation for Dijkstra'''
            start = time()
            graphs.dijkstra(0)
            end = time()
            time_dijkstra.append(end - start)
            print("Dijkstra ok, in " + str(end - start) + " s")
            '''Time calculation for Shortest_way'''
            start = time()
            graphs.shortest_way(0)
            end = time()
            time_shortest_way.append(end - start)
            print("Shortest_way ok, in " + str(end - start) + " s")
            if condition_bellman:
                '''Time calculation for Bellman_ford'''
                start = time()
                graphs.bellman_ford(0)
                end = time()
                time_bellman_ford.append(end - start)
                print("Bellman_ford ok, in " + str(end - start) + " s")
            '''Question 4.3'''
            start_tot = time()
            time_inter = np.zeros((100,))
            for j in range(100):
                node_1 = random.randint(0, (i + 1) * 10 ** 3 - 1)
                node_2 = random.randint(0, (i + 1) * 10 ** 3 - 1)
                start = time()
                graphs.shortest_way_node(node_1, node_2)
                end = time()
                time_inter[i] = end - start
            end_tot = time()
            print("Question 4.3 ok, in " + str(end_tot - start_tot) + " s")
            time_min += [float(np.amin(time_inter))]
            time_max += [float(np.amin(time_inter))]
            time_mean += [float(np.mean(time_inter))]
            time_median += [float(np.median(time_inter))]
            print("Step " + str(i + 1) + " on " + str(len(list_graph)) + " ended\n")
    else:
        '''Results for nb_time_test = 10 and alpha = 0.4'''
        time_dijkstra = [1.211676836013794, 4.412577152252197, 7.060339689254761, 13.176113843917847,
                         20.323632955551147, 27.29337978363037, 39.26716160774231, 46.7073438167572, 60.019668102264404,
                         69.2892518043518]
        time_shortest_way = [0.12880563735961914, 0.4535541534423828, 0.9880166053771973, 1.811699390411377,
                             4.234841823577881, 4.113159656524658, 5.559200286865234, 7.736715316772461,
                             10.888736486434937, 13.395088911056519]
        time_bellman_ford = []
        time_min = []
        time_max = []
        time_mean = []
        time_median = []
    return time_dijkstra, time_shortest_way, time_bellman_ford, time_min, time_max, time_mean, time_median


def second_time_test(nb_test, nb_node, condition, condition_bellman=False):
    """Calculation of the 4.2 times if condition is True or just return the times already calculated else"""
    if condition:
        list_graph = second_generation_list_graph(nb_test, nb_node)
        print("list_graph calculated !\n")
        time_dijkstra = []
        time_shortest_way = []
        time_bellman_ford = []
        time_min = []
        time_max = []
        time_mean = []
        time_median = []
        for i in range(nb_test):
            graphs = list_graph[i]
            '''Time calculation for Dijkstra'''
            start = time()
            graphs.dijkstra(0)
            end = time()
            time_dijkstra.append(end - start)
            print("Dijkstra ok, in " + str(end - start) + " s")
            '''Time calculation for Shortest_way'''
            start = time()
            graphs.shortest_way(0)
            end = time()
            time_shortest_way.append(end - start)
            print("Shortest_way ok, in " + str(end - start) + " s")
            if condition_bellman:
                '''Time calculation for Bellman_ford'''
                start = time()
                graphs.bellman_ford(0)
                end = time()
                time_bellman_ford.append(end - start)
                print("Bellman_ford ok, in " + str(end - start) + " s")
            '''Question 4.3'''
            start_tot = time()
            time_inter = np.zeros((100,))
            for j in range(100):
                node_1 = random.randint(0, nb_node - 1)
                node_2 = random.randint(0, nb_node - 1)
                start = time()
                graphs.shortest_way_node(node_1, node_2)
                end = time()
                time_inter[i] = end - start
            end_tot = time()
            print("Question 4.3 ok, in " + str(end_tot - start_tot) + " s")
            time_min += [float(np.amin(time_inter))]
            time_max += [float(np.amin(time_inter))]
            time_mean += [float(np.mean(time_inter))]
            time_median += [float(np.median(time_inter))]
            print("Step " + str(i + 1) + " on " + str(len(list_graph)) + " ended\n")
    else:
        '''Results for nb_time_test = 10 and 5000 nodes'''
        time_dijkstra = [5.172393321990967, 5.679447412490845, 6.1073033809661865, 6.741821050643921, 7.31539511680603,
                         7.788542747497559, 8.177793979644775, 8.484809398651123, 8.744366645812988, 8.942070960998535]
        time_shortest_way = [0.018529891967773438, 0.4541912078857422, 0.8362479209899902, 1.1723318099975586,
                             1.5285160541534424, 1.8614389896392822, 2.132507562637329, 2.3899898529052734,
                             2.5810956954956055, 2.7706081867218018]
        time_bellman_ford = []
        time_min = []
        time_max = []
        time_mean = []
        time_median = []
    return time_dijkstra, time_shortest_way, time_bellman_ford, time_min, time_max, time_mean, time_median


nb_time_test = 10

alpha = 0.4
first_calculation = True
times_dijkstra_1, times_shortest_way_1, times_bellman_ford_1, times_min_1, times_max_1, times_mean_1, times_median_1 = first_time_test(
    nb_time_test, alpha, first_calculation)
print(times_dijkstra_1, "\n", times_shortest_way_1, "\n", times_bellman_ford_1, "\n", times_min_1, "\n", times_max_1,
      "\n", times_mean_1, "\n", times_median_1)

n = 5000
second_calculation = True
times_dijkstra_2, times_shortest_way_2, times_bellman_ford_2, times_min_2, times_max_2, times_mean_2, times_median_2 = second_time_test(
    nb_time_test, n, second_calculation)
print(times_dijkstra_2, "\n", times_shortest_way_2, "\n", times_bellman_ford_2, "\n", times_min_2, "\n", times_max_2,
      "\n", times_mean_2, "\n", times_median_2)

'''Plot 1'''
nb_list = [i * 10 ** 3 for i in range(1, nb_time_test + 1)]

plt.figure(1)
plt.ylabel('Time (s)', fontsize=20)
plt.xlabel('Nodes number $n$', fontsize=20)
plt.title(r"Edges number = $0.4n^2$")

plt.plot(nb_list, times_dijkstra_1, label='Dijkstra')
plt.plot(nb_list, times_shortest_way_1, label="Shortest_way")
if times_bellman_ford_1:
    plt.plot(nb_list, times_bellman_ford_1, label="Bellman_ford")
plt.plot(nb_list, times_min_1, label="Time min")
plt.plot(nb_list, times_max_1, label="Time max")
plt.plot(nb_list, times_mean_1, label="Time mean")
plt.plot(nb_list, times_median_1, label="Time median")

plt.legend(loc='best')
plt.show()

'''Plot 2'''
nb_list = [int((1 / n + (0.4 - 1 / n) * j / nb_time_test) * n ** 2) for j in range(1, nb_time_test + 1)]

plt.figure(2)
plt.ylabel('Time (s)', fontsize=20)
plt.xlabel('Edges number $n$', fontsize=20)
plt.title(r"Nodes number = " + str(n))

plt.plot(nb_list, times_dijkstra_2, label='Dijkstra')
plt.plot(nb_list, times_shortest_way_2, label="Shortest_way")
if times_bellman_ford_2:
    plt.plot(nb_list, times_bellman_ford_2, label="Bellman_ford")
plt.plot(nb_list, times_min_2, label="Time min")
plt.plot(nb_list, times_max_2, label="Time max")
plt.plot(nb_list, times_mean_2, label="Time mean")
plt.plot(nb_list, times_median_2, label="Time median")

plt.legend(loc='best')
plt.show()
