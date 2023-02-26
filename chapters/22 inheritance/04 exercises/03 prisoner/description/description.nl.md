Een bekend speltheoretisch probleem is
het "Iterated Prisoner's Dilemma," in het Nederlands officieel
halfslachtig vertaald als het "geïtereerde dilemma van de gevangene." In
dit probleem spelen twee strategieën tegen elkaar over meerdere rondes.
Iedere ronde kan iedere strategie kiezen tussen twee mogelijkheden
(zonder daarbij te weten wat de andere strategie kiest): "Coöperatie"
(C) of "Defectie" (D) (vrij vertaald: "samenwerken" of "tegenwerken").
Als beide strategieën C spelen, krijgen ze allebei 3 punten. Als ze
beide D spelen, krijgen ze allebei 1 punt. Als één strategie C speelt en
één strategie D, dan krijgt de strategie die C speelt 0 punten, en de
strategie die D speelt 6 punten. Het doel van iedere strategie is zoveel
mogelijk punten te verdienen over de gehele duur van het spel.

Hieronder is een eenvoudige versie van het "Iterated Prisoner's Dilemma"
gecodeerd. Een strategie om het spel te spelen is gedefinieerd door de
class `Strategie`. Het hoofdprogramma laat twee strategieën tegen elkaar
spelen over 100 rondes (het is niet moeilijk om in het hoofdprogramma
meer dan twee strategieën tegen elkaar te laten spelen in paren, maar
dat maakt de code een stuk langer en is niet van belang voor de opgave).
De class `Strategie` heeft geen implementatie voor de methode `keuze()`.
Om een strategie te creëren, leid je een nieuwe class van `Strategie`
af, en vul je op zijn minst de `keuze()` methode in. Optioneel mag je
ook de `laatstezet()` methode invullen, en de `__init__()` methode
uitbreiden.

Implementeer de volgende strategieën:

-   `Random` speelt COOPERATIE of DEFECTIE per toeval

-   `AltijdD` speelt altijd DEFECTIE

-   `OogOmOog` start met COOPERATIE, en speelt daarna wat de
    tegenstander in de vorige ronde speelde (de `laatstezet()` methode
    krijgt altijd te zien wat de tegenstander speelde nadat een keuze
    gemaakt is)

-   `OogOmTweeOgen` start met twee keer COOPERATIE, en speelt dan
    DEFECTIE als de opponent DEFECTIE speelde in de twee voorgaande
    rondes, en anders COOPERATIE

-   `Meerderheid` start met COOPERATIE, en speelt dan wat de
    tegenstander speelde in de meerderheid van de voorgaande rondes

Als je nog meer strategieën wilt implementeren, mag dat natuurlijk. Test
sommige strategieën uit tegen elkaar door ze in te vullen bij de
toekenningen aan `strategie1` en `strategie2` (vergeet niet om ze een
naam te geven tussen de haakjes).

Merk op dat de manier waarop ik de score telling heb gecodeerd (met een
statement als `3 if c1 == COOPERATIE else 1`) een verkorte manier is om
met Python een eenvoudige conditie te schrijven, die lijkt op list
comprehension (zie hoofdstuk
13).
Dat heb ik alleen gedaan om ruimte te besparen en leesbaarheid te
verhogen; je mag dit natuurlijk ook doen met de 4 regels code die nodig
zijn om dit in een `if`-statement te zetten.

```python
COOPERATIE = 'C'
DEFECTIE = 'D'
RONDES = 100

class Strategie:
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

print( "Eind score", strategie1.name, "is", strategie1.score )
print( "Eind score", strategie2.name, "is", strategie2.score )
```
