#
# line_num.py:
#
# Muntaser Khan
#

# read filename fname from user
fname = 'test_1.txt'
# open file named 'lnum_' + fname for writing
outFile = open('lnum_' + fname,'w')
fname = open (fname, 'r') # open file for reading

# iterate over fname, line by line:
count = 1
for aline in fname:
    # add 'dddd: ' to start of line
    lineNumber = str(count).zfill(4) + ': '
    aline = lineNumber + aline
    count += 1
    #write the modified line to output file
    outFile.write(aline)

# close both files
fname.close()
outFile.close()
