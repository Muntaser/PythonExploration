#
# HTT Ch 6 code example:
#
# Section 6.8, example 2: ch04_adv

def squareit(n):
    return n * n

def cubeit(n):
    return n*n*n

def main():
    anum = int(input("Please enter a number"))
    print(squareit(anum))
    print(cubeit(anum))

print (__name__)

if __name__ == "__main__":
    main()
