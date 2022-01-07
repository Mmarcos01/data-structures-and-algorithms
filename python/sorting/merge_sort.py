def merge_sort(list):

    n = len(list)

    if n > 1:                                   # If list length is greater than 1:
        middle = len(list) //2              # Determine the middle of the list, divide it into two and represent the
        left = list[:middle]              # halves with variables of 'left' and 'right'.
        right = list[middle:]
        merge_sort(left)                # Recursively call the function on the left and right halves until the lists are split into smaller lists each containing one item
        merge_sort(right)

        i = j = k = 0                           # Declare variables 'i' , 'j' = 0 to reference left-most index of list and variable k = 0 to keep track of the index in merged array.

        while i < len(left) and j < len(right):     # While each index is less than its list length:
            if left[i] < right[j]:                                 # Begin comparisons of values between left array at index 'i' and right array at index 'j'.
                list[k] = left[i]                                   # If left index is less than right index: save it to the merged array and increment i
                i += 1
            else:                                                      # Otherwise The right index is smaller or equal to left index,
                list[k] = right[j]                                  # so save it to the merged array and increment j and k
                j += 1
            k += 1

        while i < len(left):                   # While any value is remains in left sublist: add it to the list, increment i and k
            list[k] = left[i]
            i += 1
            k += 1

        while j < len(right):                 # While any value is remains in right sublist: add it to the list, increment j and k
            list[k] = right[j]
            j += 1
            k += 1

    return list

