def rev_list(list):
  if len(list) <=1 :
    return list

  start = 0
  end = len(list) -1

  while start < end:
    temp = list[start]
    list[start] = list[end]
    list[end] = temp
    start +=1
    end -=1
  return list

def rev_list2(list1):
    if len(list1) <=1:
        return list1

    list2=[]
    length=len(list1)
    while length > 0:
        list2.append(list1[length-1])
        length = length - 1
    return list2

def rev_list3(list):
    return list[::-1]
