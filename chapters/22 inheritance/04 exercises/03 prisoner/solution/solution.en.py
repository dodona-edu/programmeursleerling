import random

COOPERATE = 'C'
DEFECT = 'D'
ROUNDS = 100

class Strategy:

    """
    >>> s = Strategy('Sam')
    >>> s.name
    'Sam'
    >>> s.score
    0
    >>> s.choice()
    NotImplemented
    >>> s.lastmove('C', 'D')
    >>> s.incscore(3)
    >>> s.score
    3
    """

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

class Random(Strategy):

    """
    Plays COOPERATE or DEFECT completely at random: overrides choice(),
    but reuses everything else from Strategy unchanged.

    >>> random.seed(1)
    >>> r = Random('Rae')
    >>> r.choice() in (COOPERATE, DEFECT)
    True
    """

    def choice( self ):
        return random.choice((COOPERATE, DEFECT))

class AlwaysDefect(Strategy):

    """
    >>> a = AlwaysDefect('Al')
    >>> a.choice()
    'D'
    >>> a.choice()
    'D'
    >>> a.lastmove('D', 'C')
    >>> a.incscore(6)
    >>> a.score
    6
    """

    def choice( self ):
        return DEFECT

class TitForTat(Strategy):

    """
    Starts with COOPERATE, then mimics whatever the opponent played on
    the previous move.

    >>> t = TitForTat('Tia')
    >>> t.choice()
    'C'
    >>> t.lastmove('C', 'D')
    >>> t.choice()
    'D'
    >>> t.lastmove('D', 'C')
    >>> t.choice()
    'C'
    """

    def __init__( self, name="" ):
        Strategy.__init__( self, name )
        self.opponentlast = COOPERATE
    def choice( self ):
        return self.opponentlast
    def lastmove( self, mymove, opponentmove ):
        self.opponentlast = opponentmove

class TitForTwoTats(Strategy):

    """
    Starts with two COOPERATEs, then plays DEFECT only if the opponent
    played DEFECT on both of the previous two moves.

    >>> t = TitForTwoTats('Toby')
    >>> t.choice()
    'C'
    >>> t.lastmove('C', 'D')
    >>> t.choice()
    'C'
    >>> t.lastmove('C', 'D')
    >>> t.choice()
    'D'
    >>> t.lastmove('D', 'C')
    >>> t.choice()
    'C'
    """

    def __init__( self, name="" ):
        Strategy.__init__( self, name )
        self.opponenthistory = []
    def choice( self ):
        if (
            len(self.opponenthistory) >= 2 and
            self.opponenthistory[-1] == DEFECT and
            self.opponenthistory[-2] == DEFECT
        ):
            return DEFECT
        return COOPERATE
    def lastmove( self, mymove, opponentmove ):
        self.opponenthistory.append(opponentmove)

class Majority(Strategy):

    """
    Starts with COOPERATE, then plays whatever the opponent played on
    the majority of the previous moves (ties go to COOPERATE).

    >>> m = Majority('Mia')
    >>> m.choice()
    'C'
    >>> m.lastmove('C', 'D')
    >>> m.lastmove('C', 'D')
    >>> m.choice()
    'D'
    >>> m.lastmove('D', 'C')
    >>> m.lastmove('D', 'C')
    >>> m.choice()
    'C'
    """

    def __init__( self, name="" ):
        Strategy.__init__( self, name )
        self.opponenthistory = []
    def choice( self ):
        if not self.opponenthistory:
            return COOPERATE
        defects = self.opponenthistory.count(DEFECT)
        cooperates = self.opponenthistory.count(COOPERATE)
        return DEFECT if defects > cooperates else COOPERATE
    def lastmove( self, mymove, opponentmove ):
        self.opponenthistory.append(opponentmove)

strategy1 = TitForTat('Tessa')
strategy2 = AlwaysDefect('Aiden')

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

if __name__ == '__main__':
    print( "End score of", strategy1.name, "is", strategy1.score )
    print( "End score of", strategy2.name, "is", strategy2.score )
    import doctest
    doctest.testmod()
