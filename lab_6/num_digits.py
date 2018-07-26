#
#   num_digits.py:
#
#       Starting code for Lab 6-3
#

def numDigits(num):
    n_str = str(num)
    return len(n_str)

def numDigits2(num):
    if num < 0:
        return len(str(num)) - 1
    else:
        return len(str(num))

def numDigits3(num):
    if num == 0:
        return 1
    if(num < 0):
        num = num * (-1)
    length = 0
    while num != 0:
        num = num // 10
        length += 1
    return length



def main():

    number = int(input("Enter a integer: "))


    # print (number, 'has', numDigits(number), 'digits.')
    #
    # print("%s has %d digits (different output)." % (number, numDigits(number)))  # alternate output
    print("%s has %d digits." % (number, numDigits2(number)))  # alternate output
    print("%s has %d digits." % (number, numDigits3(number)))  # alternate output

    # in the above, % is the old Python formatting operator:
    #
    # fmt-string % (v1,v2,...) results in each vN substituted into % slots within
    #   fmt-string, with slot types %d for int, %s for str, %f for float
    #

main()