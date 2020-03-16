from line_profiler import LineProfiler
from networkx import single_source_dijkstra_path_length


def main(params, n_runs=5):
    Gu1, Gu2 = params['Gu']
    S = params['S']
    for i in range(n_runs):
        print('Run', i + 1)
        GD = Gu1.dijkstra(S)
        GDo = Gu1.dijkstra_opti(S)
        ND = single_source_dijkstra_path_length(Gu2, S)


if __name__ == '__main__':
    from graph import UndirectedGraph as du
    from graph_generation import generate_random_graph as grg
    from random import choice

    Gu1 = grg(1000, 400000, True)
    Gu2 = Gu1.to_networkx()
    my_params = {
        'Gu': [Gu1, Gu2],
        'S': choice(Gu1.vertices)
    }

    lp = LineProfiler()
    lp.add_function(du.dijkstra)
    lp.add_function(du.shortest_way)
    lp.add_function(single_source_dijkstra_path_length)

    lp_wrapper = lp(main)
    lp_wrapper(my_params)

    lp.print_stats(output_unit=1e-3)

    stats_file = 'profile_networkx_and_graph_dijkstra.lprof'
    lp.dump_stats(stats_file)
    #print('Run the following command to display the results:')
    #print('$ python3 -m line_profiler {}'.format(stats_file))
