#
# two_aces.py:
#
# Muntaser Khan
# Would be lower than the previous random card result as it draws the top card from deck
#

import deck as d

TRIALS = 10000

def deal_card():
    deck = d.Deck()
    return deck.dealCard()

def main():
	twoAceCount = 0
	for count in range(TRIALS):

		deck = d.Deck()
		deck.shuffle()

		card1 = deal_card()
		card2 = deal_card()

		if card1._rank == 1 and card2._rank == 1:
			twoAceCount = twoAceCount + 1
			# twoAceCount += 1

	print ("Percentage of two aces is %.2f" % (100 * twoAceCount / TRIALS))

main()

