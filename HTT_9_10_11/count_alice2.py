#
# count_alice2.py:
#
#   Starting code for H7-1
#

# start with your Lab 7 count_alice and continue...
import string

FILENAME = 'alice.txt'

fvar = open(FILENAME, 'r')  # open file for reading

allwords = []  # accumulate the words in this list
final_word = [] # final list

for aline in fvar:

	line = aline.lower() # lower case it

	line = line.replace('--',' ') # replace Victorian --

	words = line.split()  # splits the line on whitespace (blanks, '\n', '\t')

	for next_word in words:

		allwords.append(next_word)  # add word + its line number as tuple to allwords


print (len(allwords))

for word in sorted(allwords):
	word = word.replace('_', '').replace('"', '').replace(',', '').replace('.', '')
	word = word.replace('-', '').replace('?', '').replace('!', '').replace("'", "")
	word = word.replace('(', '').replace(')', '').replace(':', '').replace('[', '')
	word = word.replace(']', '').replace(';', '')

	final_word.append(word)

final_word.sort()

for word in final_word:
	print(word)

fvar.close()

