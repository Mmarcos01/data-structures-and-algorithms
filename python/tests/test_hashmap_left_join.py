from hashtables.hashtable import Hashtable
import pytest
from hashtables.hashmap_left_join import hashmap_left_join

def test_proof_of_life():
    assert hashmap_left_join

def test_instantiate_hashmap():
    hashmap = Hashtable()
    assert hashmap

def test_empty_hashmap_returns_None():
    hashtable1 = Hashtable()
    hashtable2 = Hashtable()
    hashtable1.add("tomato", "soup")
    actual = hashmap_left_join(hashtable1, hashtable2)
    assert actual == None

def test_hashmap_left_join():
    hashtable1 = Hashtable()
    hashtable2 = Hashtable()
    hashtable1.add("tomato", "soup")
    hashtable2.add("beef", "stew")
    actual = hashmap_left_join(hashtable1, hashtable2)
    assert actual == ["tomato", "soup", "beef", "stew"]

def test_hashmap_left_join():
    hashtable1 = Hashtable()
    hashtable2 = Hashtable()
    hashtable1.add("tomato", "soup")
    hashtable2.add("tomato", "salad")
    actual = hashmap_left_join(hashtable1, hashtable2)
    assert actual == ["tomato", "soup", "salad"]
