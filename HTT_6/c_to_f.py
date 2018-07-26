#
# Muntaser Khan
#
# c_to_f.py
#


def c2f(celsius) :
    return round(9 * celsius/5 + 32, 2)


tempCelcius = float(input("Enter a float temperature in degree celcius"))
print(c2f(tempCelcius))



