#
# intcheck.py
#
# Author: Muntaser Khan
#

num = int(input("Enter an integer"))

# Using if-elif-else
if num > 0: print("Greater than zero")
elif num < 0: print("Less than zero")
else: print("Equals zero")

# Using if-else
def compare(N):
    if N > 0: print("Greater than zero")
    else:
        if N < 0: print("Less than zero")
        else: print("Equals zero")

def main():
    compare(num)

main()
