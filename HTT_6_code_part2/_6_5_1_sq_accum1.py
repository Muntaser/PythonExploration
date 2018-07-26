#
# HTT Ch 6 code example:
#
# Section 6.5, example 1: sq_accnum1
#

def square(x):
    runningtotal = 0 # this is the accum initialization
    for counter in range(x):
        runningtotal = runningtotal + x

    return runningtotal

toSquare = 4
squareResult = square(toSquare)
print("The result of", toSquare, "squared is", squareResult)
