#
# HTT Ch 6 code example, using PyTest:
#
# Section 6.9, example 1: ch06_distance1

import pytest

def distance(x1, y1, x2, y2):
    return 0.0

def test_Equal():
    assert distance(1, 2, 1, 2) == 0


