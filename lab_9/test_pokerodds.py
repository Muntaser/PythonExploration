'''
Lab 9-4 Module: test_pokerodds.py:

Muntaser Khan
'''

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

def buildDict(hand):
    dict = {}

    for card in hand:
        dict[card._rank] = dict.get(card._rank, 0) + 1

    # Complete this

    return dict


def hasOnePair(dict):
    # Check for EXACTLY one pair in dict and no three-of-a-kinds

    # Note there might be 2 pairs; hence the counting of pairs
    #   and there might be three-of-a-kind plus a single pair:
    #   full house

    twocount = 0
    threecount = 0
    for v in dict.values():
        if v == 2:
            twocount += 1
        elif v == 3:
            threecount += 1

    if(twocount == 1 and threecount == 0):
        return True

    return False


def hasTwoPairs(dict):
    '''
    Complete this!
    :param dict: dictionary with card ranks to check
    '''


    twocount = 0
    for v in dict.values():
        if v == 2:
            twocount += 1

    if twocount == 2:
        return True
    return False


def hasThreeOfAKind(dict):
    '''
    Complete this!
    :param dict: dictionary with card ranks to check
    '''
    threecount = 0
    for v in dict.values():
        if v == 3:
            threecount += 1

    if threecount == 1:
        return True
    return False



def hasFullHouse(dict):
    '''
    Complete this!
    :param dict: dictionary with card ranks to check
    '''

    twocount = 0
    threecount = 0
    for v in dict.values():
        if v == 2:
            twocount += 1
        elif v == 3:
            threecount += 1

    if(twocount == 1 and threecount == 1):
        return True

    return False


def hasFourOfAKind(dict):
    '''
    Complete this!
    :param dict: dictionary with card ranks to check
    '''

    fourcount = 0
    for v in dict.values():
        if v == 4:
            fourcount += 1

    if fourcount == 1:
        return True
    return False


def hasStraight(dict):
    '''
    Complete this!
    :param dict: dictionary with card ranks to check
    '''
    # five cards of sequential rank

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

    TRIALS = 10000  # int(input ("Input number of hands to test: "))

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

        if hasOnePair(dict):
            onepairCount += 1
        elif hasTwoPairs(dict):
            twopairCount += 1

        elif hasThreeOfAKind(dict):
               threeCount += 1
        elif hasFourOfAKind(dict):
               fourCount += 1
    ##        elif hasFullHouse(dict):
    ##            fourCount += 1

    # add more if you wish...

    # print out results...

    print("Number of one pair hands is: ", onepairCount)

    print("% of hands: ", 100.0 * onepairCount / TRIALS)

    print("Number of two pair hands is: ", twopairCount)

    print("% of hands: ", 100.0 * twopairCount / TRIALS)

    print("Number of three of a kind hands is: ", threeCount)

    print("% of hands: ", 100.0 * threeCount / TRIALS)

    print("Number of four of a kind hands is: ", fourCount)

    print("% of hands: ", 100.0 * fourCount / TRIALS)

# Number of one pair hands is:  4225
# % of hands:  42.25 , theoritical propbability is the same
# Number of two pair hands is:  432
# % of hands:  4.32, theoritical propbability is 4.75%
# Number of three of a kind hands is:  229
# % of hands:  2.29, theoritical propbability is 2.11%
# Number of four of a kind hands is:  2
# % of hands:  0.02, theoritical propbability is 0.024%
#The results match theoritical propbabilities

def card_example_1():
    card1 = Card()  # Card(1,3)
    card2 = Card(12, 2)
    card1._newfield = 47

    print(card1.__str__())  # long-winded form
    print(str(card2))
    print(card1._newfield)
    print(card1._rank)
    print(card1._suit)


def deck_example_1():
    '''
    Test Deck: create, print then shuffle, print again
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


if __name__ == "__main__":
    # testCard() # uncomment to test creating & calling Card methods

    deck_example_1()  # uncomment to test Deck: create, print, shuffle, print

    # test() # uncomment to test hand (list of 5 Card obj) for one pair

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


def test_two_pair():

    testhand = [Card(2, 3), Card(1, 2),
                Card(2, 1), Card(1, 3),
                Card(13, 0)]

    dict = buildDict(testhand)

    assert hasTwoPairs(dict)

def test_three_of_a_kind():

    testhand = [Card(2, 3), Card(1, 2),
                Card(2, 1), Card(2, 3),
                Card(13, 0)]

    dict = buildDict(testhand)

    assert hasThreeOfAKind(dict)

def test_four_of_a_kind():

    testhand = [Card(2, 3), Card(2, 2),
                Card(2, 1), Card(2, 3),
                Card(13, 0)]

    dict = buildDict(testhand)

    assert hasFourOfAKind(dict)

def test_full_house():

    testhand = [Card(2, 3), Card(2, 2),
                Card(2, 1), Card(13, 3),
                Card(13, 0)]

    dict = buildDict(testhand)

    assert hasFullHouse(dict)