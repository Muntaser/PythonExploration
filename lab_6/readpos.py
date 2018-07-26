#
#   readpos.py:
#
#   Muntaser Khan
#


def read_pos():
    while True:
        N = int(input("Enter an integer N >= 0: "))
        if N >= 0:
            return N
            break  # stops the loop
        else:
            print("Bad input.  Try again ", end="")


def main():
    result = read_pos()
    print (result)

main()