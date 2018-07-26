#
# Muntaser Khan
#
# patterns2.py
#

def triangle(N):
    # outer loop to handle number of rows
    # n in this case
    k = 0
    for i in range(N, 0, -1):
        for j in range(0,k):
            print(end=" ")

        # increasing k after each loop
        k = k + 2
        for j in range(0, i ):
            # printing stars
            print("* ", end="")
        # ending line after each row
        print("\r")


def hollow_box(N):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if (i == 1 or i == N or
                    j == 1 or j == N):
                print("*", end="")
            else:
                print(" ", end="")

        print()



n = int(input("Enter int N >= 0: "))
triangle(n)
hollow_box(n)

