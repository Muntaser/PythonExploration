#
# Author: Muntaser Khan
# Python program that reads integers start and stop from the user, then calculates and prints the sum of each integer ranging from start to stop
# sumrange.py
#
sum = 0
a = input("Enter 1st number")
b = input("Enter 2nd number")

for num in range(int(a), int(b) + 1):
    sum += num
print (sum) # start new line