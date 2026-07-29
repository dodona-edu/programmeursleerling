Using the definitions created in the
previous exercises, create two drawpiles. The first has the 2 of
Diamonds, King of Hearts, and 7 of Clubs (in this order). The second has
the 4 of Hearts, 3 of Hearts, and 8 of Spades (in this order). Let the
draw piles play "War!" This game is played as follows: Draw the top card
from each deck. The highest of these cards goes on the bottom of its own
deck, and the other card goes there too. The game continues until there
is only one pile left.

Hint: With this setup, the game will take 13 rounds and the first deck
wins (it has to, as it contains a card that can never be beaten by the
second deck). Do you see what a boring game "War!" is? Why children
insist on playing this – with full decks even – I'll never know.

Note: Normally when "War!" is played there are special rules for when
two cards have the same rank, but in this case the draw piles contain
only cards of a unique rank. You do not have to take into account
playing the game where that can happen, though if you want to do that,
be my guest.

### Assignment

Define the classes `Card` and `Drawpile` from the previous exercises again (your submission is graded on its own, so it cannot import anything from another exercise). A card (`Card`) is created from a suit (`'Hearts'`, `'Spades'`, `'Clubs'` or `'Diamonds'`) and a rank (`2` up to `10`, `'Jack'`, `'Queen'`, `'King'` or `'Ace'`), `repr` reads as a Python expression that creates the same card, `str` describes the card in the form `Ace of Hearts`, and the comparison operators compare two cards on their rank alone. A draw pile (`Drawpile`) is created from a list (`list`) of cards, supports `len` and indexing (index 0 is the top card), has a method `add` that puts a card at the bottom of the pile and a method `draw` that removes the top card of the pile and returns it (or `None` if the pile is empty), and its `repr` and `str` read as a Python expression that creates the same draw pile.

Write a function `war` that takes two draw piles (`Drawpile`) and lets them play the game "War!". In every round the top card is drawn from both piles. The highest of these two cards is put at the bottom of the pile it was drawn from, and the other card is then put at the bottom of that same pile. The game ends as soon as one of the two piles has run out of cards. The function must return the draw pile (`Drawpile`) that won the game, that is: the pile that still holds cards.

Note that the function changes both draw piles that are passed to it. You may assume that the two piles never hold two cards of the same rank, so that a round always has a winner, and that the game always ends.

### Example

```console?lang=python&prompt=>>>
>>> pile_1 = Drawpile([Card('Diamonds', 2), Card('Hearts', 'King'), Card('Clubs', 7)])
>>> pile_2 = Drawpile([Card('Hearts', 4), Card('Hearts', 3), Card('Spades', 8)])
>>> winner = war(pile_1, pile_2)
>>> winner is pile_1
True
>>> winner
Drawpile([Card('Spades', 8), Card('Hearts', 3), Card('Hearts', 'King'), Card('Hearts', 4), Card('Clubs', 7), Card('Diamonds', 2)])
>>> len(pile_1)
6
>>> len(pile_2)
0
```
