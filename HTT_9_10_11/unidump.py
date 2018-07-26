#
#
#  unidump.py:
#
#  Muntaser Khan
#
#  Prompt user to enter int N, then print out Unicode
#   characters from 32 through N-1, 32 per line, with
#   no intervening spaces.
#
#  At beginning of each line, we print char number N of first char per line
#   in format: 'NNNN: '
#
#

N = int(input("Enter integer N: "))

for n in range(32, N):
    if n % 32 == 0:  # start next line, then add linenum prefix
        print()
        print("%04d: "% n, end='')
    print(chr(n), '', end='')

print()
