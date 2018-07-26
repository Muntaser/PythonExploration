#
# count_alice.py:
#
# Muntaser Khan
#

import string

FILENAME = 'alice.txt'

fvar = open (FILENAME, 'r') # open file for reading

allwords = [] # accumulate the words in this list

for aline in fvar:
    words = aline.split() # splits the line on whitespace (blanks, '\n', '\t')
    for word in words:    # c
        word = word.replace(".", "")  #d
        word = word.replace("?", "")
        word = word.replace(",", "")
        word = word.replace("!", "")
        word = word.replace(":", "")
        word = word.replace(";", "")
        word = word.replace('"', "")
        word = word.replace(" ’", "") # replaces a right leaning apostrophe with empty string
        word = word.replace(" ‘", "") # replaces a left leaning apostrophe with empty string


        translator = str.maketrans('', '', string.punctuation) # e
        word = word.translate(translator)
        word = word.lower()
        allwords.append(word)

print("Count of the number of the file: " + str(len(allwords)))   # b
print(allwords)
fvar.close()


