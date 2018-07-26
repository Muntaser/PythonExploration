#
# test_leap.py
#
# Author: Muntaser Khan
#
import pytest

def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0


def test_is_leap():
    assert is_leap(2000)  == True   # Divisible by 4, 100 and 400


def test_is_leap_2():
    assert is_leap(2004)  == True   # Divisible by 4, but not 100 and 400


def test_is_leap_3():
    assert is_leap(3000)  == False   # Divisible by 4, 100 , but not 400


def test_is_leap_4():
    assert is_leap(1992)  == True   # Divisible by 4


def test_is_leap_5():
    assert is_leap(2018)  == False   # Divisible by None


def test_is_leap_6():
    assert is_leap(2020)  == True


def test_is_leap_7():
    assert is_leap(2022)  == False


def test_is_leap_8():
    assert is_leap(2023)  == False


def test_is_leap_9():
    assert is_leap(2032)  == True


def test_is_leap_10():
    assert is_leap(2001)  == False