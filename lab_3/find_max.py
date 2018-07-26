#
# L3-5: find the logical bug in the following program
#
# If none of the entered number is greater than number of ints to process, it will print out number which is wrong
# max_so_far should be initialized to 0
# To be graded for EC


number = int (input("Enter number of ints to process: "))

max_so_far = 0

for count in range(number):

    next_int = int(input("Enter next integer: "))
    max_so_far = max(max_so_far,next_int) # note the built-in max()

print("Largest entered is:", max_so_far)
