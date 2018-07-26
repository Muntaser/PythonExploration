#
# HTT Ch 3 code example:
#
# Section 3.4, example 4: db_ex3_8
#

a = input('wpisz godzine')
x = input('wpisz liczbe godzin')
int(x)
int(a)

h = x // 24
s = x % 24
print (h, s)
a = a + s
print ('godzina teraz', a)
