from linked_list.linked_list import LinkedList

class Hashtable:
    def __init__(self, size=1024):
        self.size = size
        self.buckets = [None] * self.size

    def hash(self, key):
        hash_sum = 0
        for char in key:
            numeric_value = ord(char)
            hash_sum += numeric_value
        product = hash_sum * 599
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
            # return KeyError()
            return None
        current = self.buckets[index].head
        while current:
            if current.value[0] == key:
                return current.value[1]
            current = current.next

    def contains(self, key):
        index = self.hash(key)
        if self.buckets[index] is None:
            return False
        current = self.buckets[index].head
        while current:
            if current.value[0] == key:
                return True
            current = current.next
        return False
