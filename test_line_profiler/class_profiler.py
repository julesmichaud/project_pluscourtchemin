from line_profiler import LineProfiler


def main(params, n_runs=10):

    Gd = params['Dd']
    Gu = params['Du']
    for i in range(n_runs):
        print('Run', i + 1)
        AVd = Gd.add_vertex(4)
        AVu = Gu.add_vertex(4)
        RVd = Gd.remove_vertex(4)
        RVu = Gu.remove_vertex(4)
        AEd = Gd.add_edge(1, 3)
        AEu = Gu.add_edge(1, 3)
        REd = Gd.remove_edge(1, 3)
        REu = Gu.remove_edge(1, 3)
        GId = Gd.__getitem__(1)
        GIu = Gu.__getitem__(1)


if __name__ == '__main__':
    from graph import DirectedGraph as dd, UndirectedGraph as du

    D = {i: {j: 1 for j in range(4, 100)} for i in range(4, 100)}
    Dd = D.copy()
    Dd[1] = {2: 1}
    Dd[2] = {}
    Dd[3] = {2: 1}
    Du = D.copy()
    Du[1] = {2: 1}
    Du[2] = {1: 1}
    Du[3] = {}
    Gd = dd(Dd)
    Gu = du(Du)
    my_params = {
        'Dd': Gd,
        'Du': Gu
    }

    lp = LineProfiler()
    lp.add_function(dd.add_vertex)
    lp.add_function(du.add_vertex)
    lp.add_function(dd.remove_vertex)
    lp.add_function(du.remove_vertex)
    lp.add_function(dd.add_edge)
    lp.add_function(du.add_edge)
    lp.add_function(dd.remove_edge)
    lp.add_function(du.remove_edge)
    lp.add_function(dd.__getitem__)
    lp.add_function(du.__getitem__)

    lp_wrapper = lp(main)
    lp_wrapper(my_params)

    lp.print_stats(output_unit=1e-3)

    stats_file = 'class_profiler.lprof'
    lp.dump_stats(stats_file)
