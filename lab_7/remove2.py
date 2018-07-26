#
# Muntaser Khan
# remove2.py
# Write a function that removes all occurrences of a given letter from a string using list and eval
#

def squeeze_list(alist,elt):
    for char in alist:
        if char == elt:
            alist.remove(elt)
    return alist

def main():
    list1 = eval(input("Enter a list using [...] formatting: "))
    print (squeeze_list(list1, 'B'))

main()
