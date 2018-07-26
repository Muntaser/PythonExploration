#
# Author: Muntaser Khan
#
# calcpi.py
#

import math
import random
N = input("Enter a value")

inCircle = 0
piEstimate = 0.0

for count in range(int(N)):
    x = random.uniform(-1.0,1.0)
    y = random.uniform(-1.0,1.0)

    if (math.sqrt((x - 0) ** 2 + (y - 0) ** 2) <= 1.0):
        inCircle += 1
        piEstimate = 4 * inCircle / (count + 1)

print(piEstimate)
print( "Difference" , abs(piEstimate - math.pi))


