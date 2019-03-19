from vertex import *


class PathFinder:
    __start = None
    __finish = None
    __border_points_list = None
    __extended_points = None

    def __init__(self, start, finish):
        self.__start = start
        self.__finish = finish
        self.__border_points_list = list()
        self.__border_points_list.append(list([start, 0]))
        self.__extended_points = list()

    def find_path(self):
        while len(self.__border_points_list) is not 0:
            self.__sort_border_points()
            if self.__extend_vertex():
                return self.__return_path()
        return None     # No path found!

    def __return_path(self):
        string = ""
        out_list = list()
        path = self.__border_points_list[0]
        for i in range(2, len(path)):
            string += str(path[i].get_coordinates()) + " -> "
            out_list.append(path[i].get_coordinates())
        string += str(path[0].get_coordinates())
        out_list.append(path[0].get_coordinates())
        return string, out_list

    def __sort_border_points(self):
        temp_list = sorted(self.__border_points_list, key=lambda x: x[1] + self.__heuristic_distance(x[0], self.__finish))
        self.__border_points_list = temp_list
        return None

    def __extend_vertex(self):
        if self.__border_points_list[0][0] is not self.__finish:
            working_elem = self.__border_points_list[0]
            self.__extended_points.append(working_elem[0])
            self.__border_points_list.pop(0)                                                  # TODO performance penalty
            for neighbour in working_elem[0].get_neighbours():
                if neighbour[0] not in self.__extended_points:
                    temp_elem = [neighbour[0], working_elem[1] + neighbour[1]] + working_elem[2:] + [working_elem[0]]
                    self.__border_points_list.append(temp_elem)
            return False
        else:
            return True

    @staticmethod
    def __heuristic_distance(some_vertex, other_vertex):
        assert (len(some_vertex.get_coordinates()) == len(other_vertex.get_coordinates()))
        d = sum([abs(x[0]**2 - x[1]**2) for x in zip(some_vertex.get_coords(), other_vertex.get_coords())]) ** (1/2)
        return d


"""
    @staticmethod
    def heuristic_distance(some_vertex, other_vertex):
        d1 = [x**2 for x in some_vertex.get_coordinates()]
        d2 = [x**2 for x in other_vertex.get_coordinates()]

        dist = 0
        for i in range(len(d1)):
            dist += abs(d1[i] - d2[i])
        dist **= 1/2

        return dist
"""
