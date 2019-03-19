from vertex import *


class ListToGraphGenerator:
    __list = None
    __y_dim = None
    __ver_dict = None

    def __init__(self, init_list):
        self.__list = init_list
        self.__y_dim = len(init_list)
        self.__ver_dict = {}

    def __get_start_and_finish_coordinates(self):
        return self.__list[0][0], self.__list[len(self.__list) - 1][1]

    def create_graph(self):
        """
        creates a graph from given list of weighted edges

        :return: returns a tuple containing beginning and end vertex object
        """
        for edge in self.__list:
            ver = []
            for i in range(2):
                if str(edge[i]) in self.__ver_dict:
                    ver.append(self.__ver_dict[str(edge[i])])
                else:
                    ver.append(Vertex(edge[i]))
                    self.__ver_dict.update({str(edge[i]): ver[len(ver) - 1]})
            ver[0].add_new_neighbours(ver[1], edge[2])
            ver[1].add_new_neighbours(ver[0], edge[2])

        _ = self.__get_start_and_finish_coordinates()
        return self.__ver_dict[str(_[0])], self.__ver_dict[str(_[1])]
