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
        """
        :return: returns None, if no path was found, or tuple, where first element is string representing shortest path
        consisting of sequence of multidimensional points separated with ' -> ', and a second element of the returned
        tuple is a list of points in the same sequence as in first element of tuple
        """
        while len(self.__border_points_list) is not 0:
            self.__sort_border_points()
            if self.__extend_vertex():
                return self.__return_path()
        return None     # No path found!

    def __return_path(self):
        """
        :return: returns tuple, where first element is string representing shortest path
        consisting of sequence of multidimensional points separated with ' -> ', and a second element of the returned
        tuple is a list of points in the same sequence as in first element of tuple
        """
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
        """
        Sorts given points by sum of heuristic distance and cost up to that point
        """
        _ = sorted(self.__border_points_list, key=lambda x: x[1] + self.__heuristic_distance(x[0], self.__finish))
        self.__border_points_list = _

    def __extend_vertex(self):
        """
        :return: returns True only if current best point sorted with heuristic is the destination
        """
        if self.__border_points_list[0][0] is  self.__finish:
            return True

        working_elem = self.__border_points_list[0]
        self.__extended_points.append(working_elem[0])
        self.__border_points_list.pop(0)                                                  # TODO performance penalty
        for neighbour in working_elem[0].get_neighbours():
            if neighbour[0] not in self.__extended_points:
                temp_elem = [neighbour[0], working_elem[1] + neighbour[1]] + working_elem[2:] + [working_elem[0]]
                self.__border_points_list.append(temp_elem)
        return False

    @staticmethod
    def __heuristic_distance(some_vertex, other_vertex):
        """
        Calculates distance between 2 hyperdimensional points using Pythagorean theorem

        :param some_vertex: list containing coordinates of point in hyperdimension
        :param other_vertex: list containing coordinates of the other point in hyperdimension
        :return: returns distance between 2 points in hyperdimension
        """
        assert (len(some_vertex.get_coordinates()) == len(other_vertex.get_coordinates()))
        d = sum([abs(x[0]**2 - x[1]**2) for x in zip(some_vertex.get_coords(), other_vertex.get_coords())]) ** (1/2)
        return d
