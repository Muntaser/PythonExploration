#
# HTT Ch 3 code example:
#
# Section 3.4, example 5: db_ex3_9
#

current_time_str = input("What is the current time (in hours 0-23)?")
str_time = input("What time is it now?")
str_wait_time = input("What is the number of nours to wait?")
time = int(str_time)
wai_time = int(str_wait_time)

time_when_alarm_go_off = time + wait_time
print(time_when_alarm_go_off)
