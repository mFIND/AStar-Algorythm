import random


class GraphGenerator:
    __spread = None
    __rand_state = None

    __n_of_dim = None
    __n_of_ver = None
    __max_range = None

    __min_edge = None
    __max_edge = None
    __n_of_edge = None

    __min_n_of_ver = None
    __max_n_of_ver = None

    __gauss_mean = None
    __gauss_sigma = None

    def __init__(self, spread=1, min_n_of_ver=10, max_n_of_ver=100, gauss_mean=0.3, gauss_sigma=0.25):
        """
        :param spread: how far apart points should be spread (purely abstract)
        :param min_n_of_ver: min number of vertexes
        :param max_n_of_ver: max number of vertexes
        :param gauss_mean: when in between minimum number of edges and maximum number of edges mean should be,
        normalized to (0, 1)
        :param gauss_sigma: sigma of gaussian distribution for number of edges, normalized to (0, 1)
        """
        random.seed(random._urandom(10))
        self.__rand_state = random.getstate()
        self.__spread = spread * (10 ** 4)
        self.__min_n_of_ver = min_n_of_ver
        self.__max_n_of_ver = max_n_of_ver
        self.__gauss_mean = gauss_mean
        self.__gauss_sigma = gauss_sigma

    @staticmethod
    def __dist(in_list):
        """
        Computes reduced distance between 2 multi dimensional points

        :param in_list: list, where 2 first elements are lists of coordinates of the 1st and 2nd point in hyper space
        :return: returns distance between 2 multi dimensional points increased by random number from (0.5 to 1)
        """
        d = sum([abs(x[0] ** 2 - x[1] ** 2) for x in zip(in_list[0], in_list[1])]) ** (1 / 2)
        d = int(d * abs(random.random() - 0.5) + 1)
        return d

    def generate_edges(self):
        """
        :return: returns list{0} consisting of lists{1}, where list{1} represents an edge in a weighted graph.
        For that, list{1} contains 2 lists{2}[0-1], and a weight as integer. lists{2} represent multidimensional points
        """
        random.setstate(self.__rand_state)

        self.__n_of_dim = random.randrange(1, 10)
        self.__n_of_ver = random.randrange(self.__min_n_of_ver, self.__max_n_of_ver)

        self.__max_range = int(self.__spread / (self.__n_of_dim ** 3))

        self.__min_edge = self.__n_of_ver
        self.__max_edge = (self.__n_of_ver * (self.__n_of_ver - 1)) / 3

        self.__n_of_edge = random.gauss(self.__min_edge + (self.__max_edge - self.__min_edge) * self.__gauss_mean,
                                        (self.__max_edge - self.__min_edge) * self.__gauss_sigma)

        if self.__n_of_edge < self.__min_edge:
            self.__n_of_edge = self.__min_edge
        elif self.__n_of_edge > self.__max_edge:
            self.__n_of_edge = self.__max_edge
        self.__n_of_edge = int(self.__n_of_edge)

        vertex = [[random.randrange(self.__max_range) for _ in range(self.__n_of_dim)] for _ in range(self.__n_of_ver)]

        created_pairs = list()
        for x in range(self.__n_of_edge):
            while True:
                v = sorted([vertex[random.randrange(len(vertex))], vertex[random.randrange(len(vertex))]])
                if v not in created_pairs:
                    created_pairs.append(v)
                    break

        for x in range(len(created_pairs)):
            # noinspection PyTypeChecker
            created_pairs[x].append(self.__dist(created_pairs[x]))

        self.__rand_state = random.getstate()
        return created_pairs
