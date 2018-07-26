'''
Represents a standard deck of 52 playing cards,
requiring Card import
'''

#
# out_riffle.py:
#
# 	Starting code for L10-1
#

import random
import card

class Deck():
	"""
	Represents a deck of 52 standard playing cards,
		as a list of Card refs
	"""

	def __init__(self):
		'''
		Initialize deck: field _cards is list containing
			52 Card refs, initially
		:return: nothing
		'''

		self._cards = []
		for rank in range(1, 14):
			for suit in range(4):
				c = card.Card(rank, suit)
				self._cards.append(c)

	def __str__(self):
		'''
		"Stringified" deck: string of Card named,
		with \n for easier reading
		:return:
		'''
		toreturn = ''

		# for index in range(len(self._cards)):
		#     self._cards[index]

		for c in self._cards:
			temp = str(c)  # temp is the stringified card
			toreturn = toreturn + temp + "\n"  # note \n at end

		return toreturn

	def shuffle(self):
		random.shuffle(self._cards)  # note random function to do this

	def dealCard(self):
		toreturn = self._cards.pop(0)  # get and remove top card from deck
		return toreturn

	## L10-1: add new method randomCard()

	def randomCard(self):
		rrank = random.randint(1,13)
		rsuit = random.randint(0,3) # randrange(0,4)
		toreturn = card.Card(rrank,rsuit)
		return toreturn

	## L10-3: add new method dealHand()

	def dealHand(self):
		hand = []
		for count in range(5):
			nextcard = self.dealCard()
			hand.append(nextcard)
		return hand

	## L10-4: add new method outRiffle()

	def outRiffle(self):

		half1 = []
		half2 = []

		# _cards is list inside this deck with current

		for count in range(len(self._cards) // 2):
			half1.append(self.dealCard())

		for card in self._cards:
			half2.append(card)

		self._cards=[]
		for card in half1:
			self._cards.append(card)
			self._cards.append(half2.pop(0))

		if len(half2) > 0:
			self._cards.append(half2.pop(0))

def main():
	'''
	Create, print then shuffle, print again
	Then deal first two cards and print, along with bottom card
	'''
	deck = Deck()
	print(str(deck))

	print("Now we shuffle:\n")

	deck.shuffle()
	print(str(deck))

	c = deck.dealCard()

	c2 = deck.dealCard()

	print("The first card dealt is", str(c), "and the second is", str(c2))
	print("Bottom of deck is", deck._cards[-1])  # can't hide the implementation!

	print ('#')

if __name__ == "__main__":
	main()
