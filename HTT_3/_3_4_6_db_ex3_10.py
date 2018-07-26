#
# HTT Ch 3 code example:
#
# Section 3.4, example 6: db_ex3_10
#

n = input("What time is it now (in hours)?")
n = imt(n)
m = input("How many hours do you want to wait?")
m = int(m)
q = m % 12
print("The time is now", q)
