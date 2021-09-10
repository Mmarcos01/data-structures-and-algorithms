import pytest
from hashtables.hashtable import  Hashtable

def test_hasthtable_exists():
    hashtable = Hashtable()
    assert hashtable

def test_hash_consistency():
    hashtable = Hashtable()
    key = "purple"
    index = hashtable.hash(key)
    actual = hashtable.hash(key)
    assert actual == index

def test_same_index():
    hashtable = Hashtable()
    key_a = "abcde"
    key_b = "edabc"
    assert hashtable.hash(key_a) == hashtable.hash(key_b)

def test_different_index():
    hashtable = Hashtable()
    key_a = "ababab"
    key_b = "ababac"
    assert hashtable.hash(key_a) != hashtable.hash(key_b)

def test_add():
    hashtable = Hashtable()
    index = hashtable.hash("tomato")
    assert hashtable.buckets[index] is None
    hashtable.add("tomato", "soup")
    bucket = hashtable.buckets[index]
    assert bucket

def test_get():
    hashtable = Hashtable()
    hashtable.add("tomato", "soup")
    find = hashtable.get("tomato")
    assert find == "soup"

def test_contains_true():
    hashtable = Hashtable()
    hashtable.add("red", 1)
    hashtable.add("blue", 2)
    assert hashtable.contains("blue") == True

def test_contains_false():
    hashtable = Hashtable()
    hashtable.add("red", 1)
    hashtable.add("blue", 2)
    assert hashtable.contains("green") == False
