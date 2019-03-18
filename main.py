import os

from pip._vendor.distlib.compat import raw_input

from path_finder import PathFinder
from read_list_from_file import *
from generate_graph_from_list import *

TEMPORARY_FILENAME = raw_input("Input filename: ")

if True is True:  # TODO delete this block of code
    edges = [
        [[0, 0, 0], [4, 5, 6], 4],
        [[4, 5, 6], [1, 3, 9], 6],
        [[4, 7, 1], [1, 3, 9], 3],
        [[4, 7, 1], [4, 0, 4], 9],
    ]

    try:
        with open(TEMPORARY_FILENAME, "x") as temp_file:  # write, not append
            for i in range(len(edges)):
                temp_file.write(str(edges[i]) + '\n')
    except FileExistsError:
        print("File already exists! Please run program once again with different file name.")
        exit(1)
    except FileNotFoundError:
        print("Enter a name next time!")
        exit(2)


list_reader = ListReader(TEMPORARY_FILENAME)
other_edge = list_reader.get_list()

del list_reader

graphGenerator = GraphGenerator(other_edge)
graph = graphGenerator.create_graph()
start_end_coords = graphGenerator.get_start_and_finish_coordinates()

del graphGenerator

pathFinder = PathFinder(graph[0], graph[1])

""" lets live that there so we can later check what method is actually faster"""
# temp_edge = [int(s) for s in temp_str.replace('[', '').replace(']', '').split(',')]
# other_edge = list_to_nested_list(temp_edge)


# file is automatically closed, because it was opened with ''''with'''', so we can safely remove it now
os.remove(TEMPORARY_FILENAME)

print("Let's compare initial and read-from-file lists:")
print("1st: ", type(edges), edges)
print("3rd: ", type(other_edge), other_edge)

print(start_end_coords)

print("*-" * 15, '*', sep='')
print(pathFinder.find_path())
#pathFinder.debug()
