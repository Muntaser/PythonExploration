import pytest

def calc_three(x, y, z):
    return x/y + z

def test_answer_1(): # start unit test function with test_
    assert calc_three(10,5,2) == 4