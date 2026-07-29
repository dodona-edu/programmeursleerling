Schrijf een boter-kaas-eieren programma dat
twee mensen het spel samen laat spelen. Om de beurt vraagt het programma
iedere speler om de rij en de kolom waar ze een teken willen plaatsen.
Zorg ervoor dat het programma alleen een rij/kolom combinatie toestaat
die binnen het bord valt en leeg is. Als een speler heeft gewonnen,
eindigt het spel. Als het bord vol is, eindigt het spel ook, met een
gelijkspel.

Dit is een redelijk lang programma om te schrijven (60 regels code of
zo). Gebruik maken van functies helpt. Ik raad je aan een functie
`toon\_bord()` te schrijven die het bord als parameter krijgt en die het
laat zien. Maak ook een functie `neemRijKolom()` die de gebruiker om een
rij/kolom combinatie vraagt en die controleert of het een legale invoer
betreft. Maak ook een functie `winnaar()` die controleert of het bord
een winnaar heeft. Houd bij wie aan de beurt is middels een variabele
`speler` in het hoofdprogramma, die je kunt meegeven aan een functie als
argument als de functie dit moet weten. Ikzelf bouw ook altijd een
functie `opponent()` die de speler als argument krijgt en de andere
speler teruggeeft; een dergelijke functie kan gemakkelijk gebruikt
worden om van speler te wisselen na een zet.

Het hoofdprogramma zal er ongeveer als volgt uitzien (in pseudo-code):

    toon bord
    while True:
        vraag om de rij
        vraag om de kolom
        if de rij/kolom combinatie al bezet is:
            geef een foutboodschap
            continue
        plaats een markering voor de speler op de rij/kolom
        toon bord
        if er is een winnaar:
            feliciteer winnaar
            break
        if bord is vol:
            zeg dat het gelijkspel is
            break
        wissel spelers

### Opgave

Stel het bord voor als een lijst (`list`) van drie rijen, waarbij elke rij zelf een lijst (`list`) is van drie strings (`str`): `X` voor een cel die door de eerste speler ingenomen is, `O` voor een cel die door de tweede speler ingenomen is, en `.` voor een lege cel. De rijen en de kolommen worden genummerd van 1 tot en met 3. Schrijf de volgende vijf functies, en gebruik ze om het hoofdprogramma te schrijven dat hierboven geschetst wordt.

- Schrijf een functie `opponent` waaraan een speler (`X` of `O`) moet doorgegeven worden. De functie moet de andere speler teruggeven.

- Schrijf een functie `toon_bord` waaraan een bord moet doorgegeven worden. De functie moet het bord afdrukken, voorafgegaan door een regel met de kolomnummers, en met voor elke rij haar rijnummer. Scheid de cellen van een rij door één spatie.

- Schrijf een functie `plaats` waaraan een bord, een speler, een rij en een kolom moeten doorgegeven worden. Als de gegeven rij en kolom op het bord liggen en de overeenkomstige cel nog leeg is, dan moet de functie het teken van de gegeven speler in die cel plaatsen en `True` teruggeven. Anders moet de functie het bord ongewijzigd laten en `False` teruggeven.

- Schrijf een functie `winnaar` waaraan een bord moet doorgegeven worden. Als een speler drie tekens op een rij, op een kolom of op een diagonaal heeft staan, dan moet de functie die speler teruggeven. Anders moet de functie `None` teruggeven.

- Schrijf een functie `vol` waaraan een bord moet doorgegeven worden. De functie moet een Booleaanse waarde (`bool`) teruggeven die aangeeft of alle cellen van het bord ingenomen zijn.

### Voorbeeld

```console?lang=python&prompt=>>>
>>> opponent('X')
'O'
>>> bord = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]
>>> plaats(bord, 'X', 2, 2)
True
>>> plaats(bord, 'O', 2, 2)
False
>>> plaats(bord, 'O', 4, 1)
False
>>> plaats(bord, 'O', 1, 3)
True
>>> toon_bord(bord)
  1 2 3
1 . . O
2 . X .
3 . . .
>>> winnaar(bord)
>>> vol(bord)
False
>>> toon_bord([['X', 'O', 'O'], ['.', 'X', '.'], ['O', '.', 'X']])
  1 2 3
1 X O O
2 . X .
3 O . X
>>> winnaar([['X', 'O', 'O'], ['.', 'X', '.'], ['O', '.', 'X']])
'X'
>>> vol([['X', 'O', 'X'], ['X', 'O', 'O'], ['O', 'X', 'X']])
True
```
