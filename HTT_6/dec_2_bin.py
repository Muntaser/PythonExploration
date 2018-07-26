#
# dec_2_bin.py
#
# Author: Muntaser Khan
#

decimalNum = int(input("Enter N >= 0: "))

def dec_2_bin_reversed(num):
    reversedString = ''
    while num > 0:
        reversedString += str(num % 2)
        num = num // 2
    return reversedString

def reverse(s):
    result = ''
    for ch in str(s):
        result = ch + result
    # print(result)
    return result

def dec_2_bin(decimalNum):
    return reverse(dec_2_bin_reversed(decimalNum))

print(dec_2_bin(8))