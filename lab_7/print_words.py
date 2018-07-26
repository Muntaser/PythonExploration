#
#   printwords.py:
#
#   Muntaser Khan
#

def split_into_words(big_string):
    # return big_string.splitlines()
    return big_string.split('\n')

def print_longest_1(all_words):
    maxLenSoFar = 0
    maxLenWord = ''
    for word in all_words:
        if (len(word) > maxLenSoFar):
            maxLenSoFar = len(word)
            maxLenWord = word
    return maxLenWord, maxLenSoFar

def print_longest_2(all_words):
    len_list = list()
    for word in all_words:
        len_list.append(tuple((len(word),word)))
    len_list.sort()
    return len_list.pop()


def print_longest_3(all_words):
    len_list = [tuple((len(word),word)) for word in all_words]
    len_list.sort()
    return len_list.pop()

def print_first_last_equals (all,N):
    list_first_last_equals = []
    for word in all:
        if(len(word) >= N * 2 and  word[:N] == word[N:]):
            list_first_last_equals.append(word)
    return list_first_last_equals



FILENAME = 'words_2.txt'

fvar = open (FILENAME, 'r') # open file for reading

big_string = fvar.read() # read the entire file into a single string

# you might wish to move one or more of the  following
#   into one or more of the above function bodies

allwords = split_into_words(big_string)
maxLenWord = print_longest_1(allwords)[0]
maxLenSoFar = print_longest_1(allwords)[1]

maxLenList = print_longest_2(allwords)
maxLenListComprehension = print_longest_3(allwords)

maxLenStrings = []   # c accumulator
first2last2Count = print_first_last_equals(allwords, 2) # e

# same for the following code which reports the requested stats

print ("List of all words:",allwords) # a
print ("Maximum length is %d" % maxLenSoFar) # b
print ("Strings with this length:",maxLenWord) # b

print ("Maximum length is ", maxLenList[0]) # c
print ("Strings with this length:",maxLenList[1]) # c

print ("Maximum length is ", maxLenListComprehension[0]) # d
print ("Strings with this length:",maxLenListComprehension[1]) # d

print ("Number of words with first 2 == last 2:",first2last2Count) # e

fvar.close()
