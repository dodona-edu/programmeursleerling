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
    Speelt COOPERATIE of DEFECTIE volledig per toeval: overschrijft
    enkel keuze(), en hergebruikt de rest ongewijzigd van Strategie.

    >>> random.seed(1)
    >>> r = Random('Rae')
    >>> r.keuze() in (COOPERATIE, DEFECTIE)
    True
    """

    def keuze( self ):
        return random.choice((COOPERATIE, DEFECTIE))

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
        return DEFECTIE

class OogOmOog(Strategie):

    """
    Start met COOPERATIE, en speelt daarna wat de tegenstander in de
    vorige ronde speelde.

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

    def __init__( self, name="" ):
        Strategie.__init__( self, name )
        self.opponentlast = COOPERATIE
    def keuze( self ):
        return self.opponentlast
    def laatstezet( self, mijnzet, opponentzet ):
        self.opponentlast = opponentzet

class OogOmTweeOgen(Strategie):

    """
    Start met twee keer COOPERATIE, en speelt dan DEFECTIE enkel als de
    opponent DEFECTIE speelde in de twee voorgaande rondes.

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

    def __init__( self, name="" ):
        Strategie.__init__( self, name )
        self.opponenthistory = []
    def keuze( self ):
        if (
            len(self.opponenthistory) >= 2 and
            self.opponenthistory[-1] == DEFECTIE and
            self.opponenthistory[-2] == DEFECTIE
        ):
            return DEFECTIE
        return COOPERATIE
    def laatstezet( self, mijnzet, opponentzet ):
        self.opponenthistory.append(opponentzet)

class Meerderheid(Strategie):

    """
    Start met COOPERATIE, en speelt dan wat de tegenstander speelde in
    de meerderheid van de voorgaande rondes (bij gelijke stand:
    COOPERATIE).

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

    def __init__( self, name="" ):
        Strategie.__init__( self, name )
        self.opponenthistory = []
    def keuze( self ):
        if not self.opponenthistory:
            return COOPERATIE
        defecties = self.opponenthistory.count(DEFECTIE)
        cooperaties = self.opponenthistory.count(COOPERATIE)
        return DEFECTIE if defecties > cooperaties else COOPERATIE
    def laatstezet( self, mijnzet, opponentzet ):
        self.opponenthistory.append(opponentzet)

strategie1 = OogOmOog('Tessa')
strategie2 = AltijdD('Aiden')

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
