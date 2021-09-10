from hashtables.hashtable import Hashtable
import pytest
from hashtables.hashtable_repeats import first_repeated_word

def test_instantiate_hashamp():
    hashmap = Hashtable()
    assert hashmap


def test_empty_string_returns_None():
    string = ""
    actual = first_repeated_word(string)
    assert actual == None


def test_no_repeats_returns_None():
    string = "no repeats in this sentance"
    actual = first_repeated_word(string)
    assert actual == None


def test_will_return_first_repeated_word():
    string = "the dog is a dog is not a cat"
    actual = first_repeated_word(string)
    assert actual == "dog"


def test_function_ignores_upper_and_lower_case():
    string = "HeLLo people, hello world"
    actual = first_repeated_word(string)
    assert actual == "hello"


def test_will_not_include_punctuations_in_check():
    string = "Hello people! Hello world!?"
    actual = first_repeated_word(string)
    assert actual == "hello"
