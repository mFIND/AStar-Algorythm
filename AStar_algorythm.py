from path_finder import *
from generate_graph_from_list import *


class AStarAlgorithm:

    @staticmethod
    def solve(edges):
        graph_generator = ListToGraphGenerator(edges)
        graph = graph_generator.create_graph()
        del graph_generator
        path_finder = PathFinder(graph[0], graph[1])
        return path_finder.find_path()
