import sys

from AStar_algorythm import AStarAlgorithm

if True is False:
    import pip._vendor.distlib.compat
    from read_list_from_file import ListReader

    TEMPORARY_FILENAME = pip._vendor.distlib.compat.raw_input("Input filename: ")

    list_reader = ListReader(TEMPORARY_FILENAME)
    graph = list_reader.get_list()
    del list_reader

else:
    from graph_gen import GraphGenerator as GraphGen

    graph_gen = GraphGen(spread=1, gauss_mean=0.00001, gauss_sigma=0.0001)
    graph = graph_gen.generate_graph()

print("Graph: ", graph)

AStar = AStarAlgorithm()
solution = AStar.solve(graph)

if solution is not None:
    # print(type(solution[0]))
    # print(type(solution[1]))
    print(solution[0])
    # print(solution[1])
else:
    print("No path found!", file=sys.__stderr__)
