import os
from read_list_from_file import *
from generate_graph_from_list import *

from util import get_out_nested_list_from_list as list_to_nested_list

TEMPORARY_FILENAME = "~temp_file.txt"

edges = [
        [[0, 0, 0], [4, 5, 6], 4],
        [[1, 2, 8], [1, 3, 9], 6],
        [[9, 7, 1], [4, 7, 1], 3],
        [[5, 3, 4], [4, 0, 4], 9],
        ]

with open(TEMPORARY_FILENAME, "w") as temp_file:  # write, not append
    for i in range(len(edges)):
        temp_file.write(str(edges[i])+'\n')

list_reader = ListReader(TEMPORARY_FILENAME)
other_edge = list_reader.get_list()
graphGenerator = GraphGenerator(other_edge)
graph = graphGenerator.create_graph()

del list_reader
del graphGenerator


""" lets live that there so we can later check what method is actually faster"""
# temp_edge = [int(s) for s in temp_str.replace('[', '').replace(']', '').split(',')]
# other_edge = list_to_nested_list(temp_edge)


# file is automatically closed, because it was opened with ''''with'''', so we can safely remove it now
os.remove(TEMPORARY_FILENAME)


print("Let's compare initial and read-from-file lists:")
print("1st: ", type(edges), edges)
print("3rd: ", type(other_edge), other_edge)

print(graph)
