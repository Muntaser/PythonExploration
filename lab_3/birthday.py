import random

numstudents = int(input("enter the number of students: "))

prob_of_unique_bdays = 1.0

days_available_for_unique_birthdays = 365

for count in range(1, numstudents + 1):
    prob_of_unique_bdays = prob_of_unique_bdays * (days_available_for_unique_birthdays / 365)

    days_available_for_unique_birthdays -= 1

print ("theoretical probability that",numstudents,"students all have unique birthdays is", \
       prob_of_unique_bdays)

TRIALS = 100000
num_with_unique_bdays = 0

for count in range(TRIALS):
    bdays = [random.randint(1,365) for s in range(numstudents)] # a list comprehension!
    unique_bdays = set(bdays)
    if len(unique_bdays) == numstudents:
        num_with_unique_bdays += 1

print ("experimental probability:", (num_with_unique_bdays/TRIALS))