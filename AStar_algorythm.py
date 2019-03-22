from path_finder import *
from generate_graph_from_list import *


class AStarAlgorithm:
    __graph = None

    def __init__(self, edges):
        graph_generator = ListToGraphGenerator(edges)
        self.__graph = graph_generator.create_graph()
        del graph_generator

    def solve(self):
        """
        :param edges: takes list{0} consisting of lists{1}, where list{1} represents an edge in a weighted graph.
        For that, list{1} contains 2 lists{2}[0-1], and a weight as integer. lists{2} represent multidimensional points

        :return: returns None, if no path was found, or tuple, where first element is string representing shortest path
        consisting of sequence of multidimensional points separated with ' -> ', and a second element of the returned
        tuple is a list of points in the same sequence as in first element of tuple
        """

        path_finder = PathFinder(self.__graph[0], self.__graph[1])
        return path_finder.find_path()
