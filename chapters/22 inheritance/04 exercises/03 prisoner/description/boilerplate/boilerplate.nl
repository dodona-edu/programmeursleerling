import random

COOPERATIE = 'C'
DEFECTIE = 'D'
RONDES = 100

class Strategie:

    """
    >>> s = Strategie('Sam')
    >>> s.name
    'Sam'
    >>> s.score
    0
    >>> s.keuze()
    NotImplemented
    >>> s.laatstezet('C', 'D')
    >>> s.plusscore(3)
    >>> s.score
    3
    """

    def __init__( self, name="" ):
        self.name = name
        self.score = 0
    def keuze( self ):
        # Moet COOPERATIE of DEFECTIE retourneren
        return NotImplemented
    def laatstezet( self, mijnzet, opponentzet ):
        # Krijgt de laatste zet die gemaakt is, na keuze()
        pass
    def plusscore( self, n ):
        self.score += n

class Random(Strategie):

    """
    >>> random.seed(1)
    >>> r = Random('Rae')
    >>> r.keuze() in (COOPERATIE, DEFECTIE)
    True
    """

    def keuze( self ):
        pass

class AltijdD(Strategie):

    """
    >>> a = AltijdD('Al')
    >>> a.keuze()
    'D'
    >>> a.keuze()
    'D'
    >>> a.laatstezet('D', 'C')
    >>> a.plusscore(6)
    >>> a.score
    6
    """

    def keuze( self ):
        pass

class OogOmOog(Strategie):

    """
    >>> t = OogOmOog('Tia')
    >>> t.keuze()
    'C'
    >>> t.laatstezet('C', 'D')
    >>> t.keuze()
    'D'
    >>> t.laatstezet('D', 'C')
    >>> t.keuze()
    'C'
    """

    def keuze( self ):
        pass

class OogOmTweeOgen(Strategie):

    """
    >>> t = OogOmTweeOgen('Toby')
    >>> t.keuze()
    'C'
    >>> t.laatstezet('C', 'D')
    >>> t.keuze()
    'C'
    >>> t.laatstezet('C', 'D')
    >>> t.keuze()
    'D'
    >>> t.laatstezet('D', 'C')
    >>> t.keuze()
    'C'
    """

    def keuze( self ):
        pass

class Meerderheid(Strategie):

    """
    >>> m = Meerderheid('Mia')
    >>> m.keuze()
    'C'
    >>> m.laatstezet('C', 'D')
    >>> m.laatstezet('C', 'D')
    >>> m.keuze()
    'D'
    >>> m.laatstezet('D', 'C')
    >>> m.laatstezet('D', 'C')
    >>> m.keuze()
    'C'
    """

    def keuze( self ):
        pass

strategie1 = Strategie()
strategie2 = Strategie()

for i in range( RONDES ):
    c1 = strategie1.keuze()
    c2 = strategie2.keuze()
    if c1 == c2:
        strategie1.plusscore( 3 if c1 == COOPERATIE else 1 )
        strategie2.plusscore( 3 if c2 == COOPERATIE else 1 )
    else:
        strategie1.plusscore( 0 if c1 == COOPERATIE else 6 )
        strategie2.plusscore( 0 if c2 == COOPERATIE else 6 )
    strategie1.laatstezet( c1, c2 )
    strategie2.laatstezet( c2, c1 )

if __name__ == '__main__':
    print( "Eind score", strategie1.name, "is", strategie1.score )
    print( "Eind score", strategie2.name, "is", strategie2.score )
    import doctest
    doctest.testmod()
