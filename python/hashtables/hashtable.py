from linked_list.linked_list import LinkedList

class Hashtable:
    def __init__(self, size=1024):
        self.size = size
        self.buckets = [None] * self.size

    def hash(self, key):
        sum = 0
        for char in key:
            numeric_value = ord(char)
            sum += numeric_value
        product = sum * 599
        index = product % self.size
        return index

    def add(self, key, value):
        index = self.hash(key)
        if not self.buckets[index]:
            self.buckets[index] = LinkedList()
        bucket = self.buckets[index]
        bucket.insert([key, value])


    def get(self, key):
        index = self.hash(key)
        if self.buckets[index] is None:
            raise KeyError()
        else:
            for kv_pair in self.buckets[index]:
                if kv_pair[0] == key:
                    return kv_pair[1]
            raise KeyError()

    def contains():
        pass
