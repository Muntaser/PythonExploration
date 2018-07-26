#
# HTT Ch 6 code example:
#
# Section 6.3, extra example showing pytest
#

# import pytest ? how to install ?

import pytest

# function to test

def func(x):
    return x + 1

def test_answer_1(): # start unit test function with test_
    assert func(4) == 5

def test_answer_2(): # and we can run all such function automagically..
    assert func(46) == 47
    # oops.  our test is wrong. see what happens...

def test_answer_3():
    assert 1==1
    assert func(3)==4




