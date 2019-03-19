import random

from pip._vendor.distlib.compat import raw_input


def dist(in_list):
    d = sum([abs(x[0] ** 2 - x[1] ** 2) for x in zip(in_list[0], in_list[1])]) ** (1 / 2)
    d *= abs(random.random() - 0.5) + 0.5
    d = int(d)
    return d


COMPLEXITY = 10000

random.seed(random._urandom(10))
random.getstate()

n_of_dim = random.randrange(1, 10)
n_of_ver = random.randrange(10, 100)
max_range = int(COMPLEXITY / (n_of_dim ** 3))
min_edge = n_of_ver  # for tweaking
max_edge = (n_of_ver * (n_of_ver - 1)) / 3  # probably performance issues when near full capacity, because brute force
# n_of_edge = random.randrange(min_edge, max_edge)
n_of_edge = random.gauss((max_edge + min_edge) / 3, (max_edge - min_edge) / 4)

if n_of_edge < min_edge:
    n_of_edge = min_edge
elif n_of_edge > max_edge:
    n_of_edge = max_edge
n_of_edge = int(n_of_edge)

vertex = [[random.randrange(max_range) for y in range(n_of_dim)] for x in range(n_of_ver)]
print(vertex)

created_pairs = list()
for x in range(n_of_edge):
    while True:
        v = sorted([vertex[random.randrange(len(vertex))], vertex[random.randrange(len(vertex))]])
        if v not in created_pairs:
            created_pairs.append(v)
            break

for x in range(len(created_pairs)):
    created_pairs[x].append(dist(created_pairs[x]))

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
