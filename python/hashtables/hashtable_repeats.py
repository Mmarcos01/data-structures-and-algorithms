from hashtables.hashtable import Hashtable
import re

def first_repeated_word(string):

    if len(string) == 0:
        return None

    hash_map = Hashtable()
    lowered = string.lower()
    words_array = re.findall(r"\w+", lowered)

    for word in words_array:
        if hash_map.contains(word):
            return word
        else:
            hash_map.add(word, word)

    return None
