from line_profiler import LineProfiler


def main(params, n_runs=5):
    Gu = params['Gu']
    S = params['S']
    for i in range(n_runs):
        print('Run', i + 1)
        D = Gu.dijkstra(S)
        Do = Gu.shortest_way(S)
        Dost = Gu.shortest_way_node(0, S)


if __name__ == '__main__':
    from graph import UndirectedGraph as du
    from graph_generation import generate_random_graph as grg
    from random import choice

    Gu = grg(1000, 400000, True)
    my_params = {
        'Gu': Gu,
        'S': choice(Gu.vertices)
    }

    lp = LineProfiler()
    lp.add_function(du.dijkstra)
    lp.add_function(du.shortest_way)
    lp.add_function(du.shortest_way_node)

    lp_wrapper = lp(main)
    lp_wrapper(my_params)

    lp.print_stats(output_unit=1e-3)

    stats_file = 'profile_dijkstra_s_functions.lprof'
    lp.dump_stats(stats_file)
    #print('Run the following command to display the results:')
    #print('$ python3 -m line_profiler {}'.format(stats_file))
