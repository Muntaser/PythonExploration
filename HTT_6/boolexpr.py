#
# boolexpr.py
#
# Author: Muntaser Khan
#

import datetime

def is_in_course(month,day) :
    return datetime.date(2018, 5, 29) <= datetime.date(2018, int(month), int(day)) <= datetime.date(2018, 7, 18)

def main():
    month = input("Enter month of the year")
    day = input("Enter day of the year")

    if(is_in_course(month, day)): print('month/day is in Summer Semester')
    else: print('month/day is NOT in Summer Semester')

#Call main
main()