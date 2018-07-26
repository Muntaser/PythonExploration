#
#   wordstats.py:
#
#     Starting code for Lab 6-4
#

# we'll learn more about reading from text files in HTT11...

FILENAME = 'words.txt'

fvar = open(FILENAME, 'r')  # open file for reading

bigline = fvar.read() # read ENTIRE file into single string

# what happens when you print such a big line?
# try it, by uncommenting next line

# print (bigline)

# the following shows the printf-formatting approach in Python: old

# [L6-4a] total number of characters, including newlines

print("Number of characters is: %d" % len(bigline))

# [L6-4b] total number of words in the file
#   hint: each word ends with a newline

print("Number of words is: " , len(bigline.split('\n')) -1)
# [L6-4c] average length of a word
sumLengthWord = 0
words = bigline.split('\n')
for word in words:
    sumLengthWord += len(word)

print("Average length of a words is: ", sumLengthWord/(len(words) -1))

# [L6-4d] count of 'e' in all words
countOfLetter = 0
for word in words:
    countOfLetter += word.count("e")

print("Count of e is: ", countOfLetter)
print("Fractional count of e is: ", countOfLetter / sumLengthWord)

# [L6-4e]

def fractionalFreq(words):
    for char in "abcdefghijklmnopqrstuvwxyz":
        countOfEachLetter = 0
        for word in words:
            countOfEachLetter += word.count(char)
        print("Count of character", char,  " is: ", countOfEachLetter)
        print("Fractional count of e is: ", countOfEachLetter / sumLengthWord)

fractionalFreq(bigline.split('\n'))

fvar.close()


