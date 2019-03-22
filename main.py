from sys import __stderr__

from time import time

from AStar_algorythm import AStarAlgorithm

temp = 0

sum_time = 0
start = time()
while temp < 1000:
    temp += 1
    if True is False:
        from pip._vendor.distlib.compat import raw_input
        from read_list_from_file import ListReader

        TEMPORARY_FILENAME = raw_input("Input filename: ")

        list_reader = ListReader(TEMPORARY_FILENAME)
        graph = list_reader.get_list()
        del list_reader

    else:
        from graph_gen import GraphGenerator as GraphGen

        graph_gen = GraphGen(spread=1, gauss_mean=0.1, gauss_sigma=0.4)
        graph = graph_gen.generate_edges()

    # print("Graph: ", graph)

    AStar = AStarAlgorithm(graph)
    solution = AStar.solve()

    if solution is not None:
        # print(type(solution))
        # print(type(solution[0]))
        # print(type(solution[1]))
        print(solution[0])
        print("Length of given path: ", len(solution[1]))
        # print(solution[1])
    else:
        print("No path found!", file=__stderr__)



sum_time += (time() - start)
print(temp, "iterations with (graph generation/reading from file/printing) took:", sum_time, "secs")

