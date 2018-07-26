#
# madhava.py
#
# Author: Muntaser Khan
#
import math

numTerms = int(input("Enter the number of terms: "))
sum = 0
sign = -1
a = 1
b = 0
for num in range(numTerms):
        sign = -sign
        term = 1.0 / (a * 3 ** b )
        a = a + 2
        b = b + 1
        sum += term * sign

pi = sum * 12 ** 0.5
print("Approximate value of pi: ", pi)
print("Error: ", abs(math.pi - pi))