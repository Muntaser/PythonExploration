#
# Muntaser Khan

#remove.py
# HTT9 Exercise 8: Write a function that removes all occurrences of a given letter from a string
#

def squeeze(s,ch):
    return s.replace(ch,"")

def main():
    print(squeeze("absolutely", 'b'))

main()
