import pytest

import function_to_test as t

def test_reverse_1():
    assert t.reverse_string("moxie") == "eixom"

def test_reverse_2():
    assert t.reverse_string('x') == 'x'

def test_empty():
    assert t.reverse_string('') == ''
