class Vertex:
    __coordinates = None
    __set_of_neighbours = None
    __visited = None

    def __init__(self, coordinates):
        self.__coordinates = coordinates
        self.__set_of_neighbours = set()
        self.__visited = False

    def is_visited(self):
        return self.__visited

    def add_new_neighbours(self, other_vertex, weight):
        self.__set_of_neighbours.add((other_vertex, weight))
    # if (other_vertex, weight) not in self.__set_of_neighbours:
    #    self.__set_of_neighbours.add((other_vertex, weight))
    #    return True
    # else:
    #    return False        # TODO needed? might be used to check if data was correct

    def get_coordinates(self):
        return self.__coordinates

    def get_neighbours(self):
        return self.__set_of_neighbours
