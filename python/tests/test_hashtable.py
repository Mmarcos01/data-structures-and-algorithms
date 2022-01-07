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

def test_can_instantiate_hashtable():
    new_hashtable = Hashtable()
    assert new_hashtable
    assert new_hashtable.size == 1024
    assert len(new_hashtable.buckets) == 1024


def test_hash_function_returns_valid_index():
    hashtable = Hashtable()
    actual_index = hashtable.hash("app")
    expected = 791
    assert actual_index == expected


def test_hash_function_will_return_a_value_within_range():
    hashtable = Hashtable()
    actual = hashtable.hash("test")
    assert actual <= 1024
    assert actual >= 0


def test_hash_function_will_return_similar_value_for_similar_word():
    hashtable = Hashtable()
    key_a = "abcd"
    key_b = "dcba"
    assert hashtable.hash(key_a) == hashtable.hash(key_b)


def test_hash_function_will_produce_different_values_for_different_words():
    hashtable = Hashtable()
    key_a = "abcd"
    key_b = "efgh"
    assert hashtable.hash(key_a) != hashtable.hash(key_b)


def test_add_works_correctly():
    hashtable = Hashtable()
    index = hashtable.hash("spam")
    assert hashtable.buckets[index] is None
    hashtable.add("spam", "eggs")
    bucket = hashtable.buckets[index]
    assert bucket


def test_add_method_will_add_to_linked_list_and_handle_collisions():
    hashtable = Hashtable()
    hashtable.add("abcd", 10)
    hashtable.add("dcba", 20)
    index = hashtable.hash("abcd")
    count = 0
    current = hashtable.buckets[index].head

    while current:
        count += 1
        current = current.next
    assert count == 2


def test_get_method_returns_value_if_key_present():
    hashtable = Hashtable()
    hashtable.add("abcd", 10)
    assert hashtable.get("abcd") == 10


def test_get_method_returns_None_for_value_not_present():
    hashtable = Hashtable()
    hashtable.add("abcd", 10)
    assert hashtable.get("xyz") is None
    # assert hashtable.get("xyz") is KeyError()
    #check how to assert key error


def test_get_method_will_account_for_linked_list_with_multiple_values():
    hashtable = Hashtable()
    hashtable.add("abcd", 10)
    hashtable.add("dcba", 20)
    hashtable.add("cbad", 30)
    assert hashtable.get("dcba") == 20


def test_contains_returns_true_if_key_is_present():
    hashtable = Hashtable()
    hashtable.add("abcd", 10)
    hashtable.add("bcda", 20)
    hashtable.add("abdc", 30)
    assert hashtable.contains("abcd")


def test_contains_returns_false_if_key_is_not_present():
    hashtable = Hashtable()
    hashtable.add("abcd", 10)
    hashtable.add("bcda", 20)
    hashtable.add("abdc", 30)
    assert hashtable.contains("xyz") == False
