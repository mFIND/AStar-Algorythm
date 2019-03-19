from pip._vendor.distlib.compat import raw_input

from AStar_algorythm import *

TEMPORARY_FILENAME = raw_input("Input filename: ")


AStar = AStarAlgorythm(TEMPORARY_FILENAME)
print(AStar.solve())