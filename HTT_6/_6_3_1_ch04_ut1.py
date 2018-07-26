#
# HTT Ch 6 code example:
#
# Section 6.3, example 1: ch04_ut1
#

def square(x):
    '''raise x to the second power'''
    return x * x

import test

print('testing square function')
test.testEqual(square(10), 100)
