#
#   patterns.py:
#
#     Muntaser Khan
#

def main():

    N = int(input("Enter an integer N: "))

    # (a) single line of N *
    print("*" * N)
    print()

    # (b) square of N by N *
    for i in range(N):
        print('*' * N)

    # (c) triangle as shown
    for i in range(0, N):
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")


main()
