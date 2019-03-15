import os

from util import get_out_nested_list_from_list as list_to_nested_list

TEMPORARY_FILENAME = "~temp_file.txt"

edge = [
        [0, 0, 0],
        [4, 5, 6],
        [4]
        ]

with open(TEMPORARY_FILENAME, "w") as temp_file:  # write, not append
    temp_file.write(str(edge))

with open(TEMPORARY_FILENAME, "r") as other_temp_file:
    temp_str = other_temp_file.readline()

# file is automatically closed, because it was opened with ''''with'''', so we can safely remove it now
os.remove(TEMPORARY_FILENAME)

temp_edge = [int(s) for s in temp_str.replace('[', '').replace(']', '').split(',')]

other_edge = list_to_nested_list(temp_edge)

yet_another_way_of_calculating_edge = list(eval(temp_str))

print("Let's compare initial and read-from-file lists:")
print("1st: ", type(edge), edge)
print("2nd: ", type(other_edge), other_edge)
print("3rd: ", type(yet_another_way_of_calculating_edge), yet_another_way_of_calculating_edge)
