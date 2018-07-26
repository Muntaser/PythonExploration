#
# H8-1: count_alice3.py
#
# Muntaser Khan
#


FILENAME = 'alice.txt'

fvar = open(FILENAME, 'r')  # open file for reading

allwords = []  # accumulate the words in this list, including line#

linenum = 0
for aline in fvar:

	linenum += 1 # next line

	line = aline.lower() # lower case it

	for punct in '!"$%&()*+,./:;<=>?@[\\]^_`{|}~': # remove punctuation, but leave '
		line = line.replace(punct, ' ')

	line = line.replace('--',' ') # replace Victorian --

	words = line.split()  # splits the line on whitespace (blanks, '\n', '\t')

	for w in words:
		allwords.append((w,linenum))  # add word + its line number as tuple to allwords

culled = []
allwords.sort()
# for w in allwords:
# 	print (w)

for wordtuple in allwords: # handle single quotes...

	word=wordtuple[0]

	word = word.replace('_', '').replace('"', '').replace(',', '').replace('.', '')
	word = word.replace('-', '').replace('?', '').replace('!', '').replace("'", "")
	word = word.replace('(', '').replace(')', '').replace(':', '').replace('[', '')
	word = word.replace(']', '').replace(';', '')

	if word.isalpha():
		temp = word.strip("'")
		if len(temp) > 0:
			culled.append((word.strip("'")))


culled.sort()
counts = {}

out = open('alice_words.txt', 'w')


for word in culled:
	counts[word] = counts.get(word,0) + 1

print ("%15s - %s" % ("word","count"))
for (k,v) in counts.items():
	out.write(k + " " + str(v))
	out.write('\n')
	print ("%15s - %d" % (k,v))

print (len(culled))


fvar.close()


