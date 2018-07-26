#
# test_f2c.py
#
# Author: Muntaser Khan
#

import f2c

import pytest

def test_1(): # start unit test function with test_
    assert f2c.f_to_c(32) == 0.0

def test_2():
    assert f2c.f_to_c(104) == 40.0

def test_3():
    assert f2c.f_to_c(-40.0) == -40.0

def test_4():
    assert f2c.f_to_c(96.26) == 35.7

def test_5():
    assert f2c.f_to_c(-32.26) == -35.7

def test_6():
    assert f2c.f_to_c(0.0) == -17.78

def test_7():
    assert f2c.f_to_c(70.0) == 21.11

def test_8():
    assert f2c.f_to_c(-70.0) == -56.67

def test_9():
    assert f2c.f_to_c(90) == 32.22

def test_10():
    assert f2c.f_to_c(50) == 10.0
