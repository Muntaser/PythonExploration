#
#   onestring.py:
#
#     Starting code from past Lab 6, showing file access
#


FILENAME = 'sherlock-stories.txt'

fvar = open (FILENAME, 'r') # open file for reading

bigline = fvar.read()

# What happens when you print such a big line?
#
# print (bigline)

# L7-2a: print out # of characters in line. Notice the % formatting...

print ("Number of characters is: %d" % len(bigline))

# L7-2b: print out # of words in file (one word per line).


# L7-2c: print out avg length of word (# non-newline chars/# words)


# L7-2d: print 'e' count, along with fractional frequency of 'e' among all letters


fvar.close()


