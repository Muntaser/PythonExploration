"""
anagrams.py:
Find and print all words in the largest set of anagram-like words
Muntaser Khan
"""


def makeSorted(w):
    charlist = sorted(w)
    sort_done  = ''.join(charlist)
    return sort_done



wordFile = open("wordstest.txt","r")

# Initialize anagrams as empty dict

anagrams = {}

count = 0
for word in wordFile:

    # Strip trailing newline

    word = word.strip() # word[:-1]

    # Create sort_done: sorted chars in stripped word

    sort_done = makeSorted(word)
    
    # If sort_done already in anagrams dictionary as key:
    #   Append stripped word to anagrams[sort_done]
    #          (adding to list of all words having same chars)
    # else:
    #   Set anagrams[sort_done] to new list with only stripped word
    #          ([word])

    if sort_done in anagrams:
        anagrams[sort_done].append(word)
    else:
        anagrams[sort_done] = [word]


wordFile.close()

anagram_freq = []

# for each list value v in anagrams
#      append ((len(v),v)) to anagram_freq

for v in anagrams.values():
    anagram_freq.append( (len(v),v) )

# sort anagram_freq in reverse order, which orders by length of list v
# anagram_freq.sort(reverse=False)
# print(anagram_freq.pop())  #Print out the largest set of words who are all anagrams of each other

anagram_freq.sort(reverse=True)

# print first 20 values of anagram_freq

for elt in anagram_freq[:20]:
    print (elt)
