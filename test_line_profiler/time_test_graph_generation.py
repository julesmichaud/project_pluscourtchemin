from graph_generation import generate_random_graph, generate_random_community_graph
from line_profiler import LineProfiler


def main(params, n_runs=5):
    [nodes, edges] = params['ggGRG']
    [nodes_commu, p_intra, p_inter] = params['ggGRCG']
    for i in range(n_runs):
        print('Run', i + 1)
        Gu = generate_random_graph(nodes, edges)
        Gd = generate_random_graph(nodes, edges, True)
        G = generate_random_community_graph(nodes_commu, p_intra, p_inter)


if __name__ == '__main__':
    my_params = {
        'ggGRG': [1000, 400000],
        'ggGRCG': [[100 for i in range(10)], 0.5, 0.3]
    }

    lp = LineProfiler()
    lp.add_function(generate_random_graph)
    lp.add_function(generate_random_community_graph)
    lp_wrapper = lp(main)
    lp_wrapper(my_params)

    lp.print_stats(output_unit=1e-3)

    stats_file = 'profile_generation_graph.lprof'
    lp.dump_stats(stats_file)
    #print('Run the following command to display the results:')
    #print('$ python3 -m line_profiler {}'.format(stats_file))
