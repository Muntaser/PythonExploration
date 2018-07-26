def reverse_string(s):
    result = '' # accumulator string
    for ch in s: # iterates through every char of str s
        result = ch + result

    return result

# print (reverse_string("moxie"))