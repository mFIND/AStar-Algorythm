def get_out_nested_list_from_list(ints_list):
    print(len(ints_list))
    our_list = list()
    for i in range(3):
        temp_list = []
        for j in range((len(ints_list) - 1) / 2 if i < 2 else 1):
            temp_list.append(ints_list[3 * i + j])
        our_list.append(temp_list)
    return our_list