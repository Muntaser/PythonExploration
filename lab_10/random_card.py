#
# random_card.py:
#
#  Muntaser Khan
#

import deck as d

TRIALS = 10000

def random_card():
    deck = d.Deck()
    return deck.randomCard()

def main():

	twoAceCount = 0
	for count in range(TRIALS):

		card1 = random_card()
		card2 = random_card()

		if card1._rank == 1 and card2._rank == 1:
			twoAceCount += 1

	print ("Percentage of two aces is %.2f" % (100 * twoAceCount / TRIALS))

main()