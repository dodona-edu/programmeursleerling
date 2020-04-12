A **standard card deck** includes 52 different cards, evenly distributed over four **suits**: 13 clubs (**♣**), 13 diamonds (**♦**{:style="color:red;"}), 13 hearts (**♥**{:style="color:red;"}) and 13 spades (**♠**). Clubs and spades are black, whereas diamonds and hearts are red. Each suit includes thirteen **ranks**: two through ten (with each card depicting that many symbols of its suit), jack, queen, king (each depicted with a symbol of its suit) and ace (depicting a single symbol of its suit). Commercial card decks may also include anywhere from one to six jokers, but we do not take these into account here.

### Assignment

Each card of a standard 52-card deck is represented by a string (`str`) that contains the **rank** of the card, followed by its **suit**:

- ranks: `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `J` (jack), `Q` (queen), `K` (king) and `A` (ace)

- suits: `C` (clubs; **♣**), `D` (diamonds; **♦**{:style="color:red;"}), `H` (hearts; **♥**{:style="color:red;"}) and `S` (spades; **♠**)

As such, the ace of spades is for example represented as `AS`, the ten of hearts as `10H` and the king of clubs as `KC`.

Write a function `deck` that takes no arguments. The function must return a (`list`) containing a random shuffle of the representations of all 52 cards in a standard card deck.

### Example

```console?lang=python&prompt=>>>
>>> deck()
['5H', '6D', '9H', 'QD', '9S', '4C', '5C', '8S', '5S', 'KC', '6C', '2C', '6S', 'KS', '7D', '3H', '3D', 'QS', '7H', '7S', 'AC', '2S', 'AS', 'AD', '9D', '8H', '4S', '7C', '3C', '8C', 'AH', 'KD', '10D', 'JH', '8D', '4H', '10C', 'JC', 'JS', 'QC', '6H', '3S', '5D', '4D', 'JD', '2H', '10S', '10H', 'KH', '9C', 'QH', '2D']
```
