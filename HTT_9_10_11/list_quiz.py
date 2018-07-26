#
# list_quiz.py:
# Muntaser Khan
# H7-3
#

# Short one-question quiz on HTT10 (Lists) to user about aliasing of list

print ('''\nEnter the output of the following code: 

        x = [7, 3, 1, 4, 0]
        y = x
        y[2] = 1000
        print(x)

		''')

answer = eval(input("? ")) # note the trick with eval(), which allows lists to be entered

if answer == [7, 3, 1000, 4, 0]:
	print ('\nCorrect!')
else:
	print ('\nSorry, that is incorrect.')

print ('''
Since x and y both reference the same list, changes to one also change the other.

If we change the 3rd element of list y from 1 to 1000, the 3rd element of x also changes to 1000

print(x) thus yields: 

[7, 3, 1000, 4, 0]

''')