def insertion_sort(list):
    for i in range(1, len(list)):
  
        temp = list[i]
        position = i - 1

        while position >= 0:
            if list[position] > temp:
                list[position + 1] = list[position]
                position = position -1
            else:
                break    

        list[position + 1] = temp
    return list 

