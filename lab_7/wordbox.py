#
# Muntaser Khan
#
# wordbox.py
#

word = input("Enter a word: ")
newWord = (word+word).lower()
i = len(word)
for num in range(len(word)):
    print(newWord[num:i])
    i += 1
