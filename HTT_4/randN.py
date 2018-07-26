#
# Author: Muntaser Khan
#
# randN.py
#

import random
numRolls = input("Enter number of rolls")

numRolls = int(numRolls)
sum = 0

for num in range(numRolls):
    sum += random.randint(1,6)

print(sum)
average = sum/numRolls
print("Average: ", average)