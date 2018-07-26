#
# HTT Ch 6 code example using PyTest:
#
# Section 6.9, example 1: ch06_distancefinal

# import test
import pytest

def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    result = dsquared**0.5
    return result

def test_Equal1():
    assert distance(1,2, 1,2) == 0

def test_Equal2():
    assert distance(1,2, 4,6) == 5

def test_Equal3():
    assert distance(0,0, 1,1) == 1.414213 # be careful comparing floats!!!
