SUITS = ('Hearts', 'Spades', 'Clubs', 'Diamonds')
RANKS = (2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace')

class Card:

    """
    >>> card_1 = Card('Hearts', 'Ace')
    >>> card_2 = Card('Spades', 'King')
    >>> card_3 = Card('Clubs', 'King')
    >>> card_1
    Card('Hearts', 'Ace')
    >>> print(card_2)
    King of Spades
    >>> card_1 == card_2
    False
    >>> card_2 == card_3
    True
    >>> card_1 > card_2
    True
    >>> card_2 >= card_3
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

if __name__ == '__main__':
    import doctest
    doctest.testmod()
