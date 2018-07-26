"""
exceptions.py
Define read_float_gt0() so it throws exception if float <=0.0 is read,
otherwise return the float
Muntaser Khan

"""

def read_float_gt0():
	float_str = input ("Enter a float > 0.0: ")
	to_return = float(float_str) # may raise ValueError
	if to_return <= 0.0:
		raise Exception
	return to_return

def main():

	while True:
		try:
			print (read_float_gt0())
			break
		except ValueError:
			print ("Bad float entered.  Retry.")
		except Exception:
			print ("Float <= 0.0 entered. Retry.")

main()