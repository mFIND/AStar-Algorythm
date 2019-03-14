def get_out_nested_list_from_string(string):
    our_list = list()
    for i in range(3):
        temp_list = []
        for j in range(3 if i < 2 else 1):
            temp_list.append(string[3 * i + j])
        our_list.append(temp_list)
    return our_list