#
# speeding.py
#
# Author: Muntaser Khan
#


def findFine(speedLimit, measuredSpeed):
    if measuredSpeed <= speedLimit:
        print("The speed is legal")
    elif measuredSpeed <= 90:
        return "The speed is illegal and the amount of fine: $", 50 + 5 * (measuredSpeed - speedLimit)
    else:
        return "The speed is illegal and the amount of fine: $", 250 + 5 * (measuredSpeed - speedLimit)


def main():
    speedLimit = float(input("Enter the speed limit in mph: "))
    measuredSpeed = float(input("Enter the measured speed in mph: "))

    print(findFine(speedLimit, measuredSpeed))

# Call main
main()