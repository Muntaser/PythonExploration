#
# Muntaser Khan
#
# Test cases for c_to_f.py
#

import pytest
import c_to_f
# function to test

def test_answer_1(): # start unit test function with test_
    assert c_to_f.c2f(0.0) == 32.0

def test_answer_2():
    assert c_to_f.c2f(40) == 104

def test_answer_3():
    assert c_to_f.c2f(-40.0) == -40.0

def test_answer_4():
    assert c_to_f.c2f(35.7) == 96.26

def test_answer_5():
    assert c_to_f.c2f(-35.7) == -32.26