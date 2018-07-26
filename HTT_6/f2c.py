#
# f2c.py
#
# Author: Muntaser Khan
#

def f_to_c(fahr):
   return round((fahr - 32) * (5/9), 2)

def main():
    tempFahr = float(input("Enter temperature in fahrenheit"))
    print(f_to_c(tempFahr))

print (__name__)

if __name__ == "__main__":
    main()
