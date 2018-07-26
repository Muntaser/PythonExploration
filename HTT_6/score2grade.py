#
# score2grade.py
#
# Author: Muntaser Khan
#

def findGrade(score):
    if score < 0 or score > 100:
        print("Bad input")
    elif score >= 90 or score <= 100:
        return "A"
    elif score >= 80 or score <= 89:
        return "B"
    elif score >= 70 or score <= 79:
        return "C"
    elif score >= 60 or score <= 69:
        return "D"
    elif score >= 0 or score <= 59:
        return "F"

def main():
    score = int(input("Enter score in the range from 0 to 100: "))
    print(findGrade(score))

# Call main
main()
