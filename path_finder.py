from collections import deque


class PathFinder:
    __start = None
    __goal = None
    __border_points_list = None
    __extended_points = None

    def __init__(self, start, finish):
        self.__start = start
        self.__goal = finish
        self.__border_points_list = deque()
        self.__border_points_list.append(list([start, 0, self.__heuristic_distance(start, self.__goal)]))
        self.__extended_points = set()

    def find_path(self):
        """
        :return: returns None, if no path was found, or tuple, where first element is string representing shortest path
        consisting of sequence of multidimensional points separated with ' -> ', and a second element of the returned
        tuple is a list of points in the same sequence as in first element of tuple
        """
        while len(self.__border_points_list) is not 0:
            if self.__extend_vertex():
                return self.__return_path()
        return None  # No path found!

    def __return_path(self):
        """
        :return: returns tuple, where first element is string representing shortest path
        consisting of sequence of multidimensional points separated with ' -> ', and a second element of the returned
        tuple is a list of points in the same sequence as in first element of tuple
        """
        string = ""
        out_list = list()
        path = self.__border_points_list[0]
        for i in range(3, len(path)):
            string += str(path[i].get_coordinates()) + " -> "
            out_list.append(path[i].get_coordinates())
        string += str(path[0].get_coordinates())
        out_list.append(path[0].get_coordinates())
        return string, out_list

    def __insert_into_border_points(self, elem):
        """
        Inserts given element into border_points deque by approximated path length
        """
        _ = 0
        if len(self.__border_points_list) != 0:
            while self.__border_points_list[0][2] < elem[2] and _ < len(self.__border_points_list):
                self.__border_points_list.rotate(-1)
                _ += 1
            if _ == len(self.__border_points_list):
                _ = 1
        self.__border_points_list.appendleft(elem)
        self.__border_points_list.rotate(_)

    def __extend_vertex(self):
        """
        :return: returns True only if current best point sorted with heuristic is the destination
        """
        if self.__border_points_list[0][0] is self.__goal:
            return True

        working_elem = self.__border_points_list.popleft()
        self.__extended_points.add(str(working_elem[0])[-11:-2])

        for neighbour in working_elem[0].get_neighbours():
            if str(neighbour[0])[-11:-2] not in self.__extended_points:
                _ = working_elem[1] + neighbour[1]  # distance from beginning to this point
                temp_elem = [neighbour[0], _, _ + self.__heuristic_distance(neighbour[0], self.__goal)]
                temp_elem += working_elem[3:] + [working_elem[0]]
                self.__insert_into_border_points(temp_elem)
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
        _ = sum([abs(x[0] ** 2 - x[1] ** 2) for x in zip(some_vertex.get_coords(), other_vertex.get_coords())]) ** (
                1 / 2)
        return _
