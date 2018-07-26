#
# HTT Ch 6 code example:
#
# Section 6.6, quiz example: func-6-1
#

def pow(b, p):
    y = b ** p
    return y

def square(x):
    a = pow(x, 2)
    return a

n = 5
result = square(n)
print(result)

result2 = pow(2,4) # demo of calls from multiple places
print(result2)