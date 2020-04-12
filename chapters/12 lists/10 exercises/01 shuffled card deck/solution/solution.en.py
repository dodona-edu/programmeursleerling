import random

ranks = set('23456789JQKA') | {'10'}
suits = set('CDHS')

def deck():

    """
    >>> deck()
    ['5H', '6D', '9H', 'QD', '9S', '4C', '5C', '8S', '5S', 'KC', '6C', '2C', '6S', 'KS', '7D', '3H', '3D', 'QS', '7H', '7S', 'AC', '2S', 'AS', 'AD', '9D', '8H', '4S', '7C', '3C', '8C', 'AH', 'KD', '10D', 'JH', '8D', '4H', '10C', 'JC', 'JS', 'QC', '6H', '3S', '5D', '4D', 'JD', '2H', '10S', '10H', 'KH', '9C', 'QH', '2D']
    """

    cards = [rank + suit for rank in ranks for suit in suits]
    random.shuffle(cards)
    return cards

if __name__ == '__main__':
    import doctest
    doctest.testmod()
