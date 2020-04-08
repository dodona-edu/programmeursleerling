Je kunt een loop in een andere loop stoppen.

Dat is een simpele uitspraak, maar ook een van de lastigste concepten
voor veel studenten om te bevatten.

Ik zal eerst een voorbeeld geven van een dubbel-geneste loop, dus een
loop die een andere loop bevat. In dat geval spreken programmeurs vaak
over een "buitenste loop" en "binnenste loop." De binnenste loop is een
deel van het blok code van de buitenste loop.

```python
for i in range( 3 ):
    print( "De buitenste loop begint met i =", i )
    for j in range( 3 ):
        print( "    De binnenste loop begint met j =", j )
        print( "    (i,j) = ({},{})".format( i, j ) )
        print( "    De binnenste loop eindigt met j =", j )
    print( "De buitenste loop eindigt met i =", i )
```

Bestudeer deze code en output totdat je hem volledig begrijpt!

De code geeft eerst aan variabele `i` de waarde 0, en geeft dan aan
variabele `j` de waardes 0, 1, en 2. Dan geeft het aan `i` de waarde 1,
en laat `j` weer de waardes 0, 1, en 2 aannemen. Tenslotte geeft het `i`
de waarde 2, en laat `j` weer 0, 1, en 2 aannemen. Dus deze code
verwerkt alle paren `(i,j)` waarbij `i` en `j` 0, 1, of 2 zijn.

Merk op dat de waardes voor variabelen in de buitenste loop ook
beschikbaar zijn voor de binnenste loop. `i` bestaat zowel in de
buitenste als in de binnenste loop.

Stel je voor dat je alle paren `(i,j)` wilt afdrukken waarbij `i` en `j`
de waardes 0 tot en met 3 kunnen aannemen, maar `j` altijd groter moet
zijn dan `i`. Dit gaat als volgt:

```python
for i in range( 4 ):
    for j in range( i+1, 4 ):
        print( "({},{})".format( i, j ) )
```

Zie je hoe ik slim de waarde van `i` gebruik om het bereik van `j` te
bepalen?

Schrijf een programma dat alle paren `(i,j)` afdrukt, waarbij `i` en `j`
de waardes 0 tot en met 3 kunnen aannemen, maar ze nooit dezelfde waarde
mogen hebben.

Je kunt natuurlijk ook `while` loops nesten, of `for` loops en `while`
loops door elkaar heen gebruiken.

Merk op dat als je een `break` of `continue` gebruikt in een binnenste
loop, dat alleen effect heeft op de binnenste loop. Er is bijvoorbeeld
geen commando dat je in de binnenste loop kunt gebruiken dat dan zowel
de binnenste als de buitenste loop meteen afbreekt.[^7]

Als je dubbel-geneste loops begrijpt, zal het waarschijnlijk geen
verrassing zijn te horen dat je ook drievoudig-geneste loops kunt
gebruiken, of viervoudig-geneste loops, of zelfs dieper. In de praktijk
zie je echter zelden een loop die dieper genest is dan drievoudig.

```python
for i in range( 3 ):
    for j in range( 3 ):
        for k in range( 3 ):
            print( "({},{},{})".format( i, j, k ) )
```
