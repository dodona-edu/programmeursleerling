Elementen van een list kunnen zelf ook lists zijn (die ook weer lists
kunnen bevatten, etcetera). Op deze manier kun je een matrix in je
programma creëren. Bijvoorbeeld, je kunt een boter-kaas-eieren bord als
volgt bouwen (een liggend streepje is een lege cel):

```python
bord = [ ["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"] ]
```

De eerste rij van het bord is `bord[0]`, de tweede rij is `bord[1]`, en
de derde rij is `bord[2]`. Als je de eerste cel van de eerste rij wilt
benaderen, is dat `bord[0][0]`, de tweede cel is `bord[0][1]` en de
derde cel is `bord[0][2]`. Bijvoorbeeld, om een "X" in het midden van
het bord te plaatsen, en een "O" in de linkerbovenhoek, gebruik je de
code hieronder. Deze code toont ook het bord op een nette manier (met
labels op de rijen en kolommen).

```python
def toon_bord( b ):
    print( "  1 2 3" )
    for rij in range( 3 ):
        print( rij+1, end=" ")
        for kol in range( 3 ):
            print( b[rij][kol], end=" " )
        print()

bord = [ ["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"] ]
bord[1][1] = "X"
bord[0][2] = "O"
toon_bord( bord )
```
