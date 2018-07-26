#
# hand_test.py:
#
# Muntaser  Khan
#

import deck as d

def dealHand(deck):
	try:
		hand = deck.dealHand()
	except IndexError:
		deck = d.Deck()
		hand = deck.dealHand()
	return  hand

def main():

	deck = d.Deck()

	for count in range(11):
		hand = dealHand(deck)

		for card in hand:
			print (str(card),end=' -- ')
		print()

main()