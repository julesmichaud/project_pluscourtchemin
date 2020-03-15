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
                time_inter[j] = end - start
            end_tot = time()
            print("Question 4.3 ok, in " + str(end_tot - start_tot) + " s")
            time_min += [float(np.amin(time_inter))]
            time_max += [float(np.amax(time_inter))]
            time_mean += [float(np.mean(time_inter))]
            time_median += [float(np.median(time_inter))]
            print("Step " + str(i + 1) + " on " + str(len(list_graph)) + " ended\n")
    else:
        '''Results for nb_time_test = 10 and alpha = 0.4'''
        time_dijkstra = [1.4837052822113037, 4.695542573928833, 7.890499591827393, 13.954487085342407,
                         20.357801914215088, 30.33057928085327, 40.549837827682495, 48.40500068664551, 85.875803232193,
                         107.02189660072327]
        time_shortest_way = [0.12702345848083496, 0.46390557289123535, 1.0327463150024414, 1.8360981941223145,
                             2.7936763763427734, 3.996694803237915, 5.640308618545532, 7.564144611358643,
                             9.603963613510132, 12.076156616210938]
        time_bellman_ford = []
        time_min = [0.0006809234619140625, 0.010604619979858398, 0.018097400665283203, 0.04246973991394043,
                    0.046694278717041016, 0.004461765289306641, 0.06990647315979004, 0.08856773376464844,
                    0.22108793258666992, 0.36795997619628906]
        time_max = [0.1060647964477539, 1.8682007789611816, 1.019993543624878, 1.8828165531158447, 2.8135969638824463,
                    3.906810760498047, 5.389337062835693, 7.3714776039123535, 9.159630298614502, 11.417489290237427]
        time_mean = [0.06290067195892333, 0.30361576557159425, 0.6071895122528076, 1.138942036628723,
                     1.6037013125419617, 2.5721552181243896, 3.3848366045951845, 4.722408983707428, 5.913534185886383,
                     7.209934833049775]
        time_median = [0.07139980792999268, 0.32485318183898926, 0.6412447690963745, 1.3009998798370361,
                       1.6949758529663086, 2.839174270629883, 3.510979175567627, 5.4859853982925415, 6.526684403419495,
                       8.257450222969055]
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
                time_inter[j] = end - start
            end_tot = time()
            print("Question 4.3 ok, in " + str(end_tot - start_tot) + " s")
            time_min += [float(np.amin(time_inter))]
            time_max += [float(np.amax(time_inter))]
            time_mean += [float(np.mean(time_inter))]
            time_median += [float(np.median(time_inter))]
            print("Step " + str(i + 1) + " on " + str(len(list_graph)) + " ended\n")
    else:
        '''Results for nb_time_test = 10 and 5000 nodes'''
        time_dijkstra = [5.153048038482666, 5.506176948547363, 6.048036336898804, 6.701523303985596, 7.190136194229126,
                         7.733627796173096, 8.101663589477539, 8.360866785049438, 8.640639066696167, 8.816247701644897]
        time_shortest_way = [0.02442646026611328, 0.4519188404083252, 0.8293697834014893, 1.2077007293701172,
                             1.5417993068695068, 1.8859360218048096, 2.1715266704559326, 2.363393783569336,
                             2.595062255859375, 2.7069785594940186]
        time_bellman_ford = []
        time_min = [0.003783702850341797, 0.01924443244934082, 0.020061969757080078, 0.06890749931335449,
                    0.08015894889831543, 0.031990766525268555, 0.04362607002258301, 0.020394563674926758,
                    0.01499485969543457, 0.014020204544067383]
        time_max = [0.03840041160583496, 0.4723532199859619, 0.8407385349273682, 1.223907709121704, 1.557676076889038,
                    1.9269390106201172, 2.1965456008911133, 2.3920645713806152, 2.640061616897583, 2.73746657371521]
        time_mean = [0.01418015718460083, 0.2811889147758484, 0.4601639890670776, 0.7656505155563355,
                     1.0005380177497865, 1.0623896265029906, 1.3554280066490174, 1.4972508144378662, 1.71880704164505,
                     1.5691740965843202]
        time_median = [0.014207124710083008, 0.31185054779052734, 0.4618358612060547, 0.8096860647201538,
                       1.0868489742279053, 0.9326863288879395, 1.6096491813659668, 1.7150532007217407,
                       1.853645920753479, 1.6876331567764282]
    return time_dijkstra, time_shortest_way, time_bellman_ford, time_min, time_max, time_mean, time_median


nb_time_test = 10

'''4.1'''
alpha = 0.4
first_calculation = False
times_dijkstra_1, times_shortest_way_1, times_bellman_ford_1, times_min_1, times_max_1, times_mean_1, times_median_1 = first_time_test(
    nb_time_test, alpha, first_calculation)
print(times_dijkstra_1, "\n", times_shortest_way_1, "\n", times_bellman_ford_1, "\n", times_min_1, "\n", times_max_1,
      "\n", times_mean_1, "\n", times_median_1)

'''4.2'''
n = 5000
second_calculation = False
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
