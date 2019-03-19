import os

from pip._vendor.distlib.compat import raw_input

from path_finder import *
from read_list_from_file import *
from generate_graph_from_list import *

TEMPORARY_FILENAME = raw_input("Input filename: ")

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

'''
print("List of edges:")
print(other_edge)

print(start_end_coords)

print("*-" * 15, '*', sep='')
'''
print(pathFinder.find_path())

