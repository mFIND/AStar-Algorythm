import sys

from pip._vendor.distlib.compat import raw_input

from AStar_algorythm import *

TEMPORARY_FILENAME = raw_input("Input filename: ")

AStar = AStarAlgorythm(TEMPORARY_FILENAME)
solution = AStar.solve()

if solution is not None:
    print(type(solution[0]))
    print(type(solution[1]))
    print(solution[0])
    print(solution[1])
else:
    print("Error occurred!", file=sys.__stderr__)