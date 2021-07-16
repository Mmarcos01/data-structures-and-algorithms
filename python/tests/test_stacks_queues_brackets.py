import pytest
from stacks_queues.stacks_queues_brackets import validate_brackets

# ======== Validate Brackets ========

def test_empty_is_balanced():
    actual = validate_brackets("")
    expected = True
    assert actual == expected

def test_no_brackets_is_balanced():
    actual = validate_brackets("hello world")
    expected = True
    assert actual == expected

def test_balanced_one():
    actual = validate_brackets("{}")
    expected = True
    assert actual == expected

def test_balanced_two():
    actual = validate_brackets("()[[Extra Characters]]")
    expected = True
    assert actual == expected

def test_unbalanced_one():
    actual = validate_brackets("{()(")
    expected = False
    assert actual == expected

def test_unbalanced_two():
    actual = validate_brackets("()[[]][{]}")
    expected = False
    assert actual == expected

