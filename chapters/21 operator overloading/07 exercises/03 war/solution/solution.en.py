SUITS = ('Hearts', 'Spades', 'Clubs', 'Diamonds')
RANKS = (2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace')

class Card:

    """
    >>> card_1 = Card('Hearts', 'Ace')
    >>> card_2 = Card('Spades', 'King')
    >>> card_1
    Card('Hearts', 'Ace')
    >>> print(card_2)
    King of Spades
    >>> card_1 > card_2
    True
    >>> Card('Trees', 7)
    Traceback (most recent call last):
    AssertionError: invalid card
    """

    def __init__(self, suit, rank):

        assert suit in SUITS, 'invalid card'
        assert rank in RANKS, 'invalid card'

        self.suit = suit
        self.rank = rank

    def __repr__(self):

        return f'Card({self.suit!r}, {self.rank!r})'

    def __str__(self):

        return f'{self.rank} of {self.suit}'

    def __eq__(self, other):

        if isinstance(other, Card):
            return RANKS.index(self.rank) == RANKS.index(other.rank)
        return NotImplemented

    def __lt__(self, other):

        if isinstance(other, Card):
            return RANKS.index(self.rank) < RANKS.index(other.rank)
        return NotImplemented

    def __le__(self, other):

        if isinstance(other, Card):
            return RANKS.index(self.rank) <= RANKS.index(other.rank)
        return NotImplemented

    def __gt__(self, other):

        if isinstance(other, Card):
            return RANKS.index(self.rank) > RANKS.index(other.rank)
        return NotImplemented

    def __ge__(self, other):

        if isinstance(other, Card):
            return RANKS.index(self.rank) >= RANKS.index(other.rank)
        return NotImplemented

class Drawpile:

    """
    The cards are kept in a list whose first element is the top card of the
    pile and whose last element is the bottom card. Drawing a card thus
    removes the first element, and adding a card appends a new last element.

    >>> pile = Drawpile([Card('Hearts', 4), Card('Clubs', 7)])
    >>> pile
    Drawpile([Card('Hearts', 4), Card('Clubs', 7)])
    >>> len(pile)
    2
    >>> pile[0]
    Card('Hearts', 4)
    >>> pile[0] < pile[1]
    True
    >>> pile.add(Card('Spades', 'Ace'))
    >>> pile.draw()
    Card('Hearts', 4)
    >>> pile
    Drawpile([Card('Clubs', 7), Card('Spades', 'Ace')])
    >>> Drawpile().draw()
    >>> len(Drawpile())
    0
    """

    def __init__(self, cards=None):

        self.cards = [] if cards is None else list(cards)

    def __repr__(self):

        return f'Drawpile({self.cards!r})'

    def __len__(self):

        return len(self.cards)

    def __getitem__(self, index):

        return self.cards[index]

    def add(self, card):

        self.cards.append(card)

    def draw(self):

        return self.cards.pop(0) if self.cards else None

def war(pile_1, pile_2):

    """
    Every round both piles draw their top card. The highest of the two cards
    goes to the bottom of the pile it came from, and the other card follows
    it there. Two cards of the same rank cannot occur, so there is always a
    winner of the round.

    >>> pile_1 = Drawpile([Card('Diamonds', 2), Card('Hearts', 'King'), Card('Clubs', 7)])
    >>> pile_2 = Drawpile([Card('Hearts', 4), Card('Hearts', 3), Card('Spades', 8)])
    >>> war(pile_1, pile_2) is pile_1
    True
    >>> pile_1
    Drawpile([Card('Spades', 8), Card('Hearts', 3), Card('Hearts', 'King'), Card('Hearts', 4), Card('Clubs', 7), Card('Diamonds', 2)])
    >>> len(pile_2)
    0
    >>> war(Drawpile(), pile_1) is pile_1
    True
    """

    while len(pile_1) > 0 and len(pile_2) > 0:

        card_1 = pile_1.draw()
        card_2 = pile_2.draw()

        if card_1 > card_2:
            pile_1.add(card_1)
            pile_1.add(card_2)
        else:
            pile_2.add(card_2)
            pile_2.add(card_1)

    return pile_1 if len(pile_1) > 0 else pile_2

if __name__ == '__main__':
    import doctest
    doctest.testmod()
