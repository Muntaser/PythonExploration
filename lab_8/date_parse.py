#
# Muntaser Khan
#
# date_parse.py
#

def parse_date(dstring):
    stripDate = dstring.split("/")
    # split as individual strings
    month = int(stripDate[0])
    day = int(stripDate[1])
    year = int(stripDate[2])
    # return the tuple
    return (str(month).zfill(2) + ',' + str(day).zfill(2) + ',' + str(year).zfill(4))


def main():

    date = input ("Enter date in form mm/dd/yyyy: ")

    result = parse_date(date)

    print (result)

main()