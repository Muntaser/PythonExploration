#
# H8-2: test_poker_odds2.py
#
# Muntaser Khan
#

import random

SUITS = ["Clubs", "Diamonds", "Hearts", "Spades"]
RANKS = ["", "Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]


class Card():
	"""
	Represents a single playing card,
		whose rank internally is int _rank: 1..13 => "Ace".."King"
		and whose suit internally is int _suit 0..3 => "Clubs".."Spades"
	"""

	def __init__(self, rank=1, suit=3):
		'''
		Initialize card with given int suit and int rank
		:param rank:
		:param suit:
		:return:
		'''
		self._rank = rank
		self._suit = suit

	def __str__(self):
		'''
		Return the string name of this card:
		"Ace of Spades": translates int fields to strings
		:return:
		'''

		# "Ace of Spades" is string for self._rank==1, self._suit==3

		toreturn = RANKS[self._rank] + " of " + SUITS[self._suit]

		return toreturn


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
				c = Card(rank, suit)
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


def buildDict(hand):  # hand is a list [...] of Card refs
	dict = {}
	for card in hand:
		dict[card._rank] = dict.get(card._rank, 0) + 1

	# Complete this

	return dict


def hasOnePair(dict):
	# Check for EXACTLY one value of 2 in dict
	# Note there might be 2 pairs; hence the counting of pairs

	twocount = 0
	threecount = 0
	for v in dict.values():
		if v == 2:
			twocount += 1
		if v == 3:
			threecount += 1

	return twocount == 1 and threecount != 1


def hasTwoPairs(dict):
	'''
	Complete this!
	:param dict: dictionary with card ranks to check
	'''
	twocount = 0
	for v in dict.values():
		if v == 2:
			twocount += 1

	return twocount == 2


def hasThreeOfAKind(dict):
	'''
	Complete this!
	:param dict: dictionary with card ranks to check
	'''

	threecount = 0
	twocount = 0
	for v in dict.values():
		if v==3:
			threecount += 1
		elif v==2:
			twocount += 1

	return threecount==1 and twocount != 1


def hasFullHouse(dict):
	'''
	Complete this!
	:param dict: dictionary with card ranks to check
	'''

	twocount = 0
	threecount = 0
	for v in dict.values():
		if v==2:
			twocount += 1
		elif v==3:
			threecount += 1

	return twocount==1 and threecount==1

def hasFourOfAKind(dict):
	'''
	Complete this!
	:param dict: dictionary with card ranks to check
	'''

	fourcount = 0
	for v in dict.values():
		if v==4:
			return True

	return False

def hasStraight(dict):
	'''
	Complete this!
	:param dict: dictionary with card ranks to check
	'''

	return False


def hasFlush(dict):
	'''
	Complete this!
	:param dict: dictionary with card ranks to check
	'''

	return False


def hasStraightFlush(dict):
	'''
	Complete this!
	:param dict: dictionary with card ranks to check
	'''

	return False


def hasRoyalFlush(dict):
	'''
	Complete this!
	:param dict: dictionary with card ranks to check
	'''

	return False


def main():
	# finish this...

	TRIALS = 100000  # int(input ("Input number of hands to test: "))

	hand = []  # list of Card in hand

	# accumulators for different counts

	onepairCount = 0
	twopairCount = 0
	threeCount = 0
	fourCount = 0
	fullHouseCount = 0

	# more if you wish...


	for num in range(TRIALS):

		d = Deck()
		d.shuffle()
		hand = []

		for count in range(5):
			hand.append(d.dealCard())

		dict = buildDict(hand)

		doublecount = 0

		if hasOnePair(dict):
			onepairCount += 1
			doublecount += 1

		if hasTwoPairs(dict):
			twopairCount += 1
			doublecount += 1

		if hasThreeOfAKind(dict):
			threeCount += 1
			doublecount += 1

		if hasFourOfAKind(dict):
			fourCount += 1
			doublecount += 1

		if hasFullHouse(dict):
			fullHouseCount += 1
			doublecount += 1

		if doublecount > 1:
			print ("huh?")

	# add more if you wish...

	# print out results...

	print("Number of one pair hands: %d - %.4f%% is: " \
		  % (onepairCount, 100.0 * onepairCount / TRIALS))

	print("Number of two pair hands: %d - %.4f%% is: " \
		  % (twopairCount, 100.0 * twopairCount / TRIALS))

	print("Number of 3-of-a-kind hands: %d - %.4f%% is: " \
		  % (threeCount, 100.0 * threeCount / TRIALS))

	print("Number of 4-of-a-kind hands: %d - %.4f%% is: " \
		  % (fourCount, 100.0 * fourCount / TRIALS))

	print("Number of full house hands: %d - %.4f%% is: " \
		  % (fullHouseCount, 100.0 * fullHouseCount / TRIALS))


if __name__ == "__main__":

	main()  # uncomment to run general poker odds calculations

#
#-------------------------------------------------------------------------
#

def test_one_pair():

    testhand = [Card(2, 3), Card(1, 2),
				Card(3, 1), Card(13, 2),
				Card(2, 0)]

    dict = buildDict(testhand)

    assert hasOnePair(dict)

def test_one_pair_2():

    testhand = [Card(3, 3), Card(3, 0), Card(1, 2),
				Card(2, 1), Card(13, 2)
				]

    dict = buildDict(testhand)

    assert hasOnePair(dict)

def test_one_pair_3():

    testhand = [Card(3, 3), Card(2, 0), Card(1, 2),
				Card(13, 1), Card(13, 2)]

    dict = buildDict(testhand)

    assert hasOnePair(dict)


def test_two_pair():

    testhand = [Card(2, 3), Card(1, 2),
                Card(2, 1), Card(1, 3),
                Card(13, 0)]

    dict = buildDict(testhand)

    assert hasTwoPairs(dict)

def test_two_pair_2():

    testhand = [Card(3, 3), Card(3, 2),
                Card(4, 1), Card(13, 0),
                Card(4, 3)]

    dict = buildDict(testhand)

    assert hasTwoPairs(dict)

def test_two_pair_3():

    testhand = [Card(13, 3), Card(4, 4),
                Card(5, 1), Card(4, 3),
                Card(13, 0)]

    dict = buildDict(testhand)

    assert hasTwoPairs(dict)

def test_three_of_a_kind():

    testhand = [Card(2, 3), Card(1, 2),
                Card(2, 1), Card(2, 3),
                Card(13, 0)]

    dict = buildDict(testhand)

    assert hasThreeOfAKind(dict)

def test_three_of_a_kind_2():

    testhand = [Card(13, 3), Card(1, 2),
                Card(13, 1), Card(2, 3),
                Card(13, 0)]

    dict = buildDict(testhand)

    assert hasThreeOfAKind(dict)

def test_three_of_a_kind_3():

    testhand = [Card(3, 3), Card(3, 2),
                Card(3, 1), Card(2, 3),
                Card(13, 0)]

    dict = buildDict(testhand)

    assert hasThreeOfAKind(dict)

def test_four_of_a_kind():

    testhand = [Card(2, 3), Card(2, 2),
                Card(2, 1), Card(2, 3),
                Card(13, 0)]

    dict = buildDict(testhand)

    assert hasFourOfAKind(dict)

def test_four_of_a_kind_2():

    testhand = [Card(13, 3), Card(13, 2),
                Card(13, 1), Card(2, 3),
                Card(13, 0)]

    dict = buildDict(testhand)

    assert hasFourOfAKind(dict)

def test_four_of_a_kind_3():

    testhand = [Card(13, 3), Card(4, 2),
                Card(4, 1), Card(4, 3),
                Card(4, 0)]

    dict = buildDict(testhand)

    assert hasFourOfAKind(dict)

def test_full_house():

    testhand = [Card(2, 3), Card(2, 2),
                Card(2, 1), Card(13, 3),
                Card(13, 0)]

    dict = buildDict(testhand)

    assert hasFullHouse(dict)

def test_full_house_2():

    testhand = [Card(3, 3), Card(3, 2),
                Card(4, 3), Card(3, 1),
                Card(4, 0)]

    dict = buildDict(testhand)

    assert hasFullHouse(dict)

def test_full_house_3():

    testhand = [Card(5, 3), Card(5, 2),
                Card(6, 3), Card(6, 0),
                Card(5, 1)]

    dict = buildDict(testhand)

    assert hasFullHouse(dict)