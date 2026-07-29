Use the `Card` class as given
above. Now also create a `Drawpile` class. A `Drawpile` consists of a
sequence of cards. The cards are supposed to form a pile with the top
card having the lowest index, and the bottom card the highest index.
Implement the `__len__()` and `__getitem__()` methods. Create an `add()`
method to add a card to the draw pile at the bottom, and a `draw()`
method to remove the top card from a draw pile and return it. Test the
class.

### Assignment

Define the class `Card` from the previous exercise again (your submission is graded on its own, so it cannot import anything from another exercise). A card (`Card`) is created from a suit (`'Hearts'`, `'Spades'`, `'Clubs'` or `'Diamonds'`) and a rank (`2` up to `10`, `'Jack'`, `'Queen'`, `'King'` or `'Ace'`), an `AssertionError` with the message `invalid card` must be raised if either of them is invalid, `repr` reads as a Python expression that creates the same card, `str` describes the card in the form `Ace of Hearts`, and the comparison operators compare two cards on their rank alone.

Also define a class `Drawpile` that can be used to represent a draw pile of cards. One optional argument may be passed when creating a new draw pile (`Drawpile`): a list (`list`) of cards (`Card`) that make up the pile, with the top card of the pile at index 0 and the bottom card at the last index. If no argument is passed, an empty draw pile must be created.

Draw piles (`Drawpile`) must at least support the following operations:

- The builtin function `len` must return the number of cards (`int`) on the pile.

- Indexing a draw pile (`pile[i]`) must return the card (`Card`) at position $$i$$ of the pile.

- A method `add` that takes a card (`Card`) and puts it at the bottom of the pile. The method returns no value.

- A method `draw` that removes the top card of the pile and returns it (`Card`). If the pile is empty, the value `None` must be returned.

- If a draw pile is passed to the builtin functions `repr` or `str`, a string (`str`) must be returned that reads as a Python expression that creates the same draw pile.

### Example

```console?lang=python&prompt=>>>
>>> pile = Drawpile([Card('Hearts', 4), Card('Clubs', 7), Card('Spades', 'Queen')])
>>> pile
Drawpile([Card('Hearts', 4), Card('Clubs', 7), Card('Spades', 'Queen')])
>>> len(pile)
3
>>> pile[0]
Card('Hearts', 4)
>>> pile[0] < pile[2]
True
>>> pile.add(Card('Diamonds', 'Ace'))
>>> len(pile)
4
>>> pile.draw()
Card('Hearts', 4)
>>> pile
Drawpile([Card('Clubs', 7), Card('Spades', 'Queen'), Card('Diamonds', 'Ace')])

>>> empty = Drawpile()
>>> len(empty)
0
>>> empty.draw()
>>> empty.add(Card('Diamonds', 10))
>>> empty
Drawpile([Card('Diamonds', 10)])
```
