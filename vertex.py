class Vertex:
    __coordinates = None
    __list_of_neighbours = None

    def __init__(self, coordinates):
        """
        :param coordinates: coordinates of the vertex in hyperdimension
        """
        self.__coordinates = coordinates
        self.__list_of_neighbours = list()

    def add_new_neighbours(self, other_vertex, weight):
        """
        Adds an directional weighted edge to a neighbour
        :param other_vertex: neighbouring vertex
        :param weight: weight of the edge
        """
        if (other_vertex, weight) not in self.__list_of_neighbours:
            self.__list_of_neighbours.append((other_vertex, weight))

    def get_coordinates(self):
        return self.__coordinates

    def get_coords(self):
        return self.get_coordinates()

    def get_neighbours(self):
        return self.__list_of_neighbours
