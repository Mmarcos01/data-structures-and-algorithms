
def binary_search(sorted_list, value):
    low_idx = 0
    high_idx = len(sorted_list) - 1

    while low_idx <= high_idx:
        mid = (high_idx + low_idx) // 2
        if sorted_list[mid] < value:
            low_idx = mid + 1
        elif sorted_list[mid] > value:
            high_idx = mid - 1
        else:
            return mid
    return -1
