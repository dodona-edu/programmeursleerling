Maak een programma dat een vereenvoudigde
versie van het spel "Zeeslagje" speelt. De computer creëert (in het
geheugen) een matrix van 3 rijen hoog en 4 kolommen breed. De rijen zijn
genummerd 1, 2, en 3, en de kolommen hebben de letters A, B, C, en D. De
computer verstopt in drie van de cellen een "oorlogsschip." Ieder schip
is precies één cel groot. De schepen mogen elkaar noch horizontaal, noch
verticaal raken. Laat het programma de schepen per toeval plaatsen, dus
niet volgens een vastgestelde configuratie.

De computer vraagt de speler te "schieten" op cellen in de matrix. De
speler doet dat door een kolom letter en rij cijfer in te geven
(bijvoorbeeld, `"D3"`). Als de cel waarop de speler schiet niks bevat,
zegt de computer "Mis!" Als de cel een schip bevat, zegt de computer
"Raak!' en verwijdert het schip (dus als de speler nog eens zou schieten
op dezelfde cel dan is het automatisch een mis). Als de speler erin
geslaagd is alle drie de schepen tot zinken te brengen, laat de computer
zien hoeveel schoten er nodig waren, en het programma eindigt.

Om te helpen bij het debuggen van het spel, laat je de computer bij de
start de matrix tonen waarbij je kunt zien welke cellen een schip
bevatten.

Hint: Als je dit een lastige oefening vindt, start dan met een bord
waarbij je de schepen al vooraf geplaatst hebt. Als de rest van de code
werkt (en dit is niet erg moeilijk na de vorige opgave), voeg dan een
functie toe waarbij de schepen per toeval geplaatst worden, zonder dat
je controleert of ze elkaar raken. Als dat eenmaal werkt, voeg je code
toe die ervoor zorgt dat de schepen elkaar niet kunnen raken.

### Opgave

Stel de matrix voor als een lijst (`list`) van drie rijen, waarbij elke rij zelf een lijst (`list`) is van vier strings (`str`): `X` voor een cel die een schip verbergt, en `.` voor een lege cel. Naar een cel van de matrix wordt verwezen met een string (`str`) die bestaat uit haar kolomletter (`A` tot en met `D`) gevolgd door haar rijnummer (`1` tot en met `3`). Schrijf de volgende vier functies, en gebruik ze om het spel te schrijven.

- Schrijf een functie `plaats_schepen` waaraan geen argumenten moeten doorgegeven worden. De functie moet een nieuwe matrix teruggeven die drie schepen verbergt in drie willekeurig gekozen cellen. De schepen mogen elkaar noch horizontaal, noch verticaal raken.

- Schrijf een functie `toon_matrix` waaraan een matrix moet doorgegeven worden. De functie moet de matrix afdrukken, voorafgegaan door een regel met de kolomletters, en met voor elke rij haar rijnummer. Scheid de cellen van een rij door één spatie.

- Schrijf een functie `schepen` waaraan een matrix moet doorgegeven worden. De functie moet teruggeven hoeveel schepen de matrix nog verbergt.

- Schrijf een functie `schiet` waaraan een matrix en een cel moeten doorgegeven worden. Als de gegeven cel een schip verbergt, dan moet de functie dat schip van de matrix verwijderen en de string `Raak!` teruggeven. Anders moet de functie de string `Mis!` teruggeven. Als de gegeven cel niet op de matrix ligt, dan moet de functie een `AssertionError` opwerpen met de boodschap `ongeldige cel`.

### Voorbeeld

```console?lang=python&prompt=>>>
>>> matrix = [['.', '.', 'X', '.'], ['X', '.', '.', '.'], ['.', '.', 'X', '.']]
>>> toon_matrix(matrix)
  A B C D
1 . . X .
2 X . . .
3 . . X .
>>> schepen(matrix)
3
>>> schiet(matrix, 'C1')
'Raak!'
>>> schiet(matrix, 'C1')
'Mis!'
>>> schiet(matrix, 'B2')
'Mis!'
>>> schepen(matrix)
2
>>> schiet(matrix, 'E1')
Traceback (most recent call last):
AssertionError: ongeldige cel
>>> schepen(plaats_schepen())
3
```
