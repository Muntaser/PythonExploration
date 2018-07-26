#
# Author: Muntaser Khan
#
# calcpi2.py
#
import math

sum = 0
sign = -1
numTerms = input("Enter number of terms")
for count in range(int(numTerms)):
    sign = -sign
    term = 1.0 / (2 * count + 1)
    sum += term * sign

pi = sum * 4
print("Approximate value of pi: ", pi)
print("Error: ", abs(math.pi - pi))
