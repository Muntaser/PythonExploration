#
# HTT Ch 6 code example:
#
# Section 6.4, example 1: badsquare_1
#

def square(x):
    runningtotal = 0
    for counter in range(x):
        runningtotal = runningtotal + x

    return runningtotal

toSquare = 10
squareResult = square(toSquare)
print("The result of", toSquare, "squared is", squareResult)
