def array_shift(list, value):
    middle_index = int(len(list)/2)
    list_length = len(list)
    if list_length % 2 != 0:
        list.insert(middle_index + 1, value)
    else:
        list.insert(middle_index, value)
    return list
