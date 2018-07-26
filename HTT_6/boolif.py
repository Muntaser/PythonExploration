#
# boolif.py
#
# Author: Muntaser Khan
#

from datetime import timedelta, date
import datetime

def isWithin(month,day,year):
    return datetime.date(2006, 6, 14) <= datetime.date(int(year), int(month), int(day)) <= datetime.date(2016, 10, 24)

def main():
    month = input("Enter month of the year")
    day = input("Enter day of the year")
    year = input("Enter the year")

    print(isWithin(month, day, year))

#Call main
main()