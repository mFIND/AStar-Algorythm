from path_finder import *
from read_list_from_file import *
from generate_graph_from_list import *

class AStarAlgorythm:
    __FILENAME = None

    def __init__(self, name):
        self.__FILENAME = name

    def solve(self):

        list_reader = ListReader(self.__FILENAME)
        other_edge = list_reader.get_list()
        del list_reader
        graph_generator = GraphGenerator(other_edge)
        graph = graph_generator.create_graph()
        del graph_generator
        path_finder = PathFinder(graph[0], graph[1])

        return path_finder.find_path()

