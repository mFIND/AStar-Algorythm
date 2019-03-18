class Vertex:
    __coordinates = None
    __list_of_neighbours = None
    __extended = None

    def __init__(self, coordinates):
        self.__coordinates = coordinates
        self.__list_of_neighbours = list()
        self.__extended = False

    def is_visited(self):
        return self.__extended

    def add_new_neighbours(self, other_vertex, weight):
        if (other_vertex, weight) not in self.__list_of_neighbours:
            self.__list_of_neighbours.append((other_vertex, weight))
    # if (other_vertex, weight) not in self.__list_of_neighbours:
    #    self.__list_of_neighbours.add((other_vertex, weight))
    #    return True
    # else:
    #    return False        # TODO needed? might be used to check if data was correct

    def get_coordinates(self):
        return self.__coordinates

    def get_coords(self):
        return self.get_coordinates()

    def get_neighbours(self):
        return self.__list_of_neighbours
