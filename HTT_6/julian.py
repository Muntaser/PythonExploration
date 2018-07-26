#
# julian.py
#
# Author: Muntaser Khan
#
import test_leap

def julian(day,month,year):
    daynum = 31 * (month - 1) + day
    if (month > 2):
        daynum = daynum - (4 * month + 23) // 10
    if (test_leap.is_leap(year)):
        daynum = daynum + 1
    return daynum

def main():
    month = int(input("Enter month of the year"))
    day = int(input("Enter day of the year"))
    year = int(input("Enter the year"))

    print("Julian Date: ", julian(day, month, year))

# Call main
main()

