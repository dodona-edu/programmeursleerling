In the Iterated Prisoner's Dilemma, two
strategies play against each other over multiple rounds. Every round,
the strategies can decide to either Coorperate (C) or Defect (D). If
both cooperate, they both get 3 points. If both defect, they both get 1
point. If one cooperates and one defects, the one that defects gets 6
points, and the one that cooperates gets nothing. The goal for each
strategy is to score as many points as possible.

Below a simple version of the Iterated Prisoner's Dilemma is coded. A
strategy to play the game is defined by the class `Strategy`. The main
loop lets two strategies play each other for 100 rounds (it is not hard
to create a main loop that lets more than two strategies play each other
in pairs, but that increases the size of the code quite a bit and is not
important for the exercise). `Strategy` has not implemented the
`choice()` method. To create a strategy, you inherit a new class from
`Strategy`, and code the `choice()` method. Optionally you can also
implement the `lastmove()` method, and extend the `__init__()` method.

Implement the following strategies:

-   `Random` just plays COOPERATE or DEFECT at random.

-   `AlwaysDefect` always plays DEFECT.

-   `TitForTat` starts with COOPERATE, then plays what the opponent
    played on the previous move (the `lastmove()` method gets to see
    what the opponent played after a choice has been made).

-   `TitForTwoTats` starts with two COOPERATEs, then plays DEFECT if the
    opponent played DEFECT on both the previous two moves, otherwise
    COOPERATEs.

-   `Majority` starts with COOPERATE, then plays what the opponent
    played on the majority of the previous moves.

If you want to implement more strategies, be my guest. Test out some of
the strategies against each other by filling in the assignments for
`strategy1` and `strategy2` (do not forget to give them a name between
the parentheses).

Note that the shorthand way that I use in this code to write a simple
condition (with a statement like `3 if c1 == COOPERATE else 1`), which
looks like a list comprehension (see Chapter
<a href="#ch:lists" data-reference-type="ref" data-reference="ch:lists">13</a>),
is just to save some space and make the code a bit more readable. It
would be just as well to write the 4 lines of code that would be needed
to do this with a regular `if` statement.

```python
# Iterated Prisoner's Dilemma
COOPERATE = 'C'
DEFECT = 'D'
ROUNDS = 100

class Strategy:
    def __init__( self, name="" ):
        self.name = name
        self.score = 0
    def choice( self ):
        # Should return COOPERATE or DEFECT
        return NotImplemented
    def lastmove( self, mymove, opponentmove ):
        # Gets passed the last move made, after a call of choice()
        pass
    def incscore( self, n ):
        self.score += n

strategy1 = Strategy()
strategy2 = Strategy()

for i in range( ROUNDS ):
    c1 = strategy1.choice()
    c2 = strategy2.choice()
    if c1 == c2:
        strategy1.incscore( 3 if c1 == COOPERATE else 1 )
        strategy2.incscore( 3 if c2 == COOPERATE else 1 )
    else:
        strategy1.incscore( 0 if c1 == COOPERATE else 6 )
        strategy2.incscore( 0 if c2 == COOPERATE else 6 )
    strategy1.lastmove( c1, c2 )
    strategy2.lastmove( c2, c1 )

print( "End score of", strategy1.name, "is", strategy1.score )
print( "End score of", strategy2.name, "is", strategy2.score )
```
