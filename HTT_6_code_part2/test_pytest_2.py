import pytest

import function_to_test as t

def test_reverse_3():
    assert t.reverse_string("mississippi") == "ippississim"

def test_reverse_4():
    assert t.reverse_string('hello') == 'olleh'

def test_reverse_5():
    assert t.reverse_string('xyz') == 'zyx'
