class GraphGenerator:
    __list = None
    __x_dim = None
    __y_dim = None

    def __init__(self, list):
        self.__list = list
        self.__y_dim = len(list)
        self.__x_dim = len(list[0])

    def compute_graph(self):
        return self.__list[0][0], self.__list[self.__y_dim - 1][1]
