#
# out_riffle.py:
#
# Muntaser Khan
#

import card as c
import deck as d

def main():

	deck = d.Deck()
	deck.shuffle()

	original_order = str(deck)

	riffleCount = 0
	while True:

		deck.outRiffle()
		riffleCount += 1

		if str(deck) == original_order:
			print ("It took %d out riffle-shuffles" % riffleCount)
			break

main()
