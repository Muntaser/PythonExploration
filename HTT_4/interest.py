#
# Author: Muntaser Khan
# Python program that computes compound interest by using a formula that uses the exponentiation operator
# interest.py
#

P = 10000
n = 12
r = 0.08

t = input("Enter the number of years the money will be compounded for")
S = 1
for counter in range(int(t) * n):
    S = S * (1 + r / n)

finalAmount = P * S

print("Final Amount: ", finalAmount)
