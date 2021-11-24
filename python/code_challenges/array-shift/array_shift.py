def array_shift(list, value):
  middle = int(len(list)/2)
  print(middle % 2)
  if len(list) % 2 != 0:
    list.insert(middle + 1, value)
  else:
    list.insert(middle, value)
  return list
