#
# debug_2.py:
#
# L3-2: We'll run this in the PyCharm debugger to understand print()'s behavior...
#

result = ''
starting = input ("Enter a string: ")

for ch in starting:
    print (ch,end='')

print() # needed to dump string accumulating in output print buffer before program ends
