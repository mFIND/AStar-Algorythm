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
        random.seed(random._urandom(10))
        self.__rand_state = random.getstate()
        self.__spread = spread * (10 ** 4)
        self.__min_n_of_ver = min_n_of_ver
        self.__max_n_of_ver = max_n_of_ver
        self.__gauss_mean = gauss_mean
        self.__gauss_sigma = gauss_sigma

    @staticmethod
    def __dist(in_list):
        d = sum([abs(x[0] ** 2 - x[1] ** 2) for x in zip(in_list[0], in_list[1])]) ** (1 / 2)
        d *= abs(random.random() - 0.5) + 0.5
        d = int(d)
        return d

    def generate_graph(self):
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


'''


TEMPORARY_FILENAME = raw_input("Output filename: ")

try:
    with open(TEMPORARY_FILENAME, "x") as temp_file:  # write, not append
        for i in range(len(created_pairs)):
            temp_file.write(str(created_pairs[i]) + '\n')
except FileExistsError:
    print("File already exists! Please run program once again with different file name.")
    exit(1)
except FileNotFoundError:
    print("Enter a name next time!")
    exit(2)
'''
