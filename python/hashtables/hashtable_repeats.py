from hashtables.hashtable import Hashtable
import re


def first_repeated_word(string):
    hashtable = Hashtable()
    case = string.lower()
    sep_words = re.findall(r'\w+', case)
    for word in sep_words:
        hashtable.hash(word)

