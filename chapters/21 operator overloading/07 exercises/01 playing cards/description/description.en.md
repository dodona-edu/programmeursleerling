A playing card consists of a suit
(`"Hearts", "Spades", "Clubs", "Diamonds"`) and a rank
(`2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"`).
Implement a `Card` class. Implement that cards are equal when they have
an equal rank, and that the other comparisons use the ranks in the order
given above (2 lowest, Ace highest). Test the class.

### Assignment

Define a class `Card` that can be used to represent playing cards. Two arguments must be passed when creating a new card (`Card`): *i*) the suit (`str`) of the card, which must be one of `'Hearts'`, `'Spades'`, `'Clubs'` or `'Diamonds'`, and *ii*) the rank of the card, which must be one of `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10` (`int`), `'Jack'`, `'Queen'`, `'King'` or `'Ace'` (`str`). If an invalid suit or an invalid rank is passed, an `AssertionError` must be raised with the message `invalid card`.

Cards (`Card`) must at least support the following operations:

- If a card is passed to the builtin function `repr`, a string (`str`) must be returned that reads as a Python expression that creates the same card. If a card is passed to the builtin function `str`, a string (`str`) must be returned that describes the card in the form `Ace of Hearts`.

- The comparison operators `==`, `!=`, `<`, `<=`, `>` and `>=` must compare two cards based on their rank alone, using the order in which the ranks are listed above (`2` is the lowest rank and `'Ace'` the highest). The suit plays no part in these comparisons, so two cards with the same rank are equal even if their suits differ.

### Example

```console?lang=python&prompt=>>>
>>> card_1 = Card('Hearts', 'Ace')
>>> card_2 = Card('Spades', 'King')
>>> card_3 = Card('Clubs', 'King')
>>> card_1
Card('Hearts', 'Ace')
>>> print(card_2)
King of Spades
>>> str(card_3)
'King of Clubs'
>>> card_1 == card_2
False
>>> card_2 == card_3
True
>>> card_1 > card_2
True
>>> card_2 >= card_3
True
>>> card_1 < card_3
False
>>> sorted([card_1, card_2, card_3])
[Card('Spades', 'King'), Card('Clubs', 'King'), Card('Hearts', 'Ace')]
>>> Card('Trees', 7)
Traceback (most recent call last):
AssertionError: invalid card
```
