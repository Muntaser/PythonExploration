#
# HTT Ch 6 code example:
#
# Section 6.6, example from slides: workedexample
#

def print_max(a, b):
    print("The maximum of", a, "and", b, "is", max(a, b))

def print_min(a, b):
    print("The minimum of", a, "and", b, "is", min(a, b))

def max_min():
    first = int(input("Enter the first int: "))
    second = int(input("Enter the second int: "))
    print_max(first,second)
    print_min(first, second)

max_min() # call the function