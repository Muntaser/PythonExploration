#
# Muntaser Khan
#
# table.py
#

print("|  * | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 |")
print("--------------------------------------------------------")
for row in range(0,10):
    print("| "+ str(row).zfill(2), end=" | ")
    for col in range(0,10):
        print(str(row*col).zfill(2), end=" | ")
    print()
