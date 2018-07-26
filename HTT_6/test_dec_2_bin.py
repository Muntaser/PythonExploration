import pytest

# function to test
def dec_2_bin_reversed(num):
    reversedString = ''
    while num > 0:
        reversedString += str(num % 2)
        num = num // 2
    return reversedString

def reverse(s):
    result = ''
    for ch in str(s):
        result = ch + result
    # print(result)
    return result

def dec_2_bin(decimalNum):
    return reverse(dec_2_bin_reversed(decimalNum))


def test_answer_1(): # start unit test function with test_
    assert dec_2_bin(8) == '1000'

def test_answer_2():
    assert dec_2_bin(15) == '1111'

def test_answer_3():
    assert dec_2_bin(100) == '1100100'

def test_answer_4():
    assert dec_2_bin(50) == '110010'

def test_answer_5():
    assert dec_2_bin(61) == '111101'

def test_answer_6():
    assert dec_2_bin(1) == '1'

def test_answer_7():
    assert dec_2_bin(43) == '101011'

def test_answer_8():
    assert dec_2_bin(34) == '100010'

def test_answer_9():
    assert dec_2_bin(16) == '10000'

def test_answer_10():
    assert dec_2_bin(35) == '100011'