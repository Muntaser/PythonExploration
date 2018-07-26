#
# debug_5.py =>
#
# L3 extra problem:
#
# What does this do?
# We'll run it in the PyCharm debugger and find out...

starting = '0123'

result = ''
for ch in starting:
    result = result + ch + result

print (result)
