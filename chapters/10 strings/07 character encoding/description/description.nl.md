Alle computersystemen gebruiken een manier om tekens te coderen. De
basis codering die door (vrijwel) ieder systeem ondersteund wordt is de
standaard ASCII code. Dit is een 7-bits code, die 128 verschillende
tekens kan weergeven. Een aantal van deze tekens (met name die met de
laagste nummers) zijn controle tekens die een speciale functie hebben.
De meeste hiervan zijn alleen nuttig voor ouderwetse computersystemen,
maar de tabulatie, "newline," en "backspace" tekens zitten er ook
tussen. Als je alleen de tekens gebruikt die op een toetsenbord met US
configuratie voorkomen, beperk je je tot standaard ASCII tekens.

Vandaag de dag gebruiken veel systemen Unicode. Unicode ondersteunt veel
meer tekens. Er zijn verschillende manieren om tekens op te slaan als
Unicode tekens. De meest bekende is UTF-8, die één byte gebruikt voor
ieder van de ASCII tekens, maar meerdere bytes voor alle andere tekens
(een byte is een groep van 8 bits, waarbij iedere bit een 1 of een 0
bevat). Andere Unicode coderingen gebruiken meerdere bytes voor alle
tekens. Python ondersteunt UTF-8, wat betekent dat het ook reguliere
ASCII coderingen ondersteunt.

### ASCII

Hieronder zie je de ASCII tabel. De enige tekens die ik heb weggelaten
zijn de speciale tekens. Die hebben nummers nul tot en met 31, en 127.
32 is de spatie. Ik geef ook de hexadecimale code voor ieder teken weer
naast de decimale code. Die worden in een later hoofdstuk relevant.

Zoals je kunt zien heeft ieder teken een getal. Om in een Python
programma te achterhalen wat het nummer is van een teken, kun je de
`ord()` functie gebruiken. `ord("A")`, bijvoorbeeld, retourneert het
nummer van `"A"`, dat 65 is, zoals je kunt zien. De tegenhanger van
`ord()` is de `chr()` functie. `chr()` krijgt een nummer als argument,
en retourneert het teken dat hoort bij dat nummer. Bijvoorbeeld,
`chr(65)` is de letter `"A"`.

    DC HX      DC HX      DC HX      DC HX      DC HX      DC HX
    32 20      48 30 0    64 40 @    80 50 P    96 60 `   112 70 p
    33 21 !    49 31 1    65 41 A    81 51 Q    97 61 a   113 71 q
    34 22 "    50 32 2    66 42 B    82 52 R    98 62 b   114 72 r
    35 23 #    51 33 3    67 43 C    83 53 S    99 63 c   115 73 s
    36 24 $    52 34 4    68 44 D    84 54 T   100 64 d   116 74 t
    37 25 %    53 35 5    69 45 E    85 55 U   101 65 e   117 75 u
    38 26 &    54 36 6    70 46 F    86 56 V   102 66 f   118 76 v
    39 27 '    55 37 7    71 47 G    87 57 W   103 67 g   119 77 w
    40 28 (    56 38 8    72 48 H    88 58 X   104 68 h   120 78 x
    41 29 )    57 39 9    73 49 I    89 59 Y   105 69 i   121 79 y
    42 2A *    58 3A :    74 4A J    90 5A Z   106 6A j   122 7A z
    43 2B +    59 3B ;    75 4B K    91 5B [   107 6B k   123 7B {
    44 2C ,    60 3C <    76 4C L    92 5C \   108 6C l   124 7C |
    45 2D -    61 3D =    77 4D M    93 5D ]   109 6D m   125 7D }
    46 2E .    62 3E >    78 4E N    94 5E ^   110 6E n   126 7E ~
    47 2F /    63 3F ?    79 4F O    95 5F _   111 6F o

Een vergelijking tussen strings waarin alleen deze tekens gebruikt
worden, gebruikt de nummers van de teken om te bepalen welke van de
strings "kleiner" is. Bijvoorbeeld, de string `"mango"` is groter dan de
string `"mangaan"`, omdat het eerste verschil tussen de strings het
vierde teken is, wat `"o"` is voor `"mango"` en `"a"` voor `"mangaan"`.
Omdat het nummer voor `"o"` groter is dan het nummer voor `"a"`, wordt
de string `"mango"` beschouwd als groter dan de string `"mangaan"`. Dit
is feitelijk een alfabetische vergelijking. Als er tekens in de string
voorkomen die geen letters zijn, kun je in de ASCII tabel nakijken welke
als kleiner beschouwd worden. Zie hoe alle cijfers kleiner zijn dan
letters.

```python
print( ord( 'A' ) )
print( ord( 'a' ) )
print( chr( 65 ) )
print( chr( 97 ) )
print( "mango" > "mangaan" )
```

Je kunt deze nummers en tekens die ermee geassocieerd zijn gebruiken in
allerhande nuttige berekeningen. Bijvoorbeeld, als je wilt weten welke
de twaalfde letter na de `"g"` is, kun je dat als volgt berekenen:

```python
print( "De twaalfde letter na g is", chr( ord( "g" )+12 ) )
```

Om een uitgebreider voorbeeld van wat je kunt doen met codes voor tekens
te laten zien, is hier een programma dat de ASCII tabel genereert als
matrix:

```python
print( ' ', end='' )
for i in range(16):
    if i < 10:
        print( ' '+chr( ord( '0' )+i ), end='' )
    else:
        print( ' '+chr( ord( 'A' )+i-10 ), end='' )
print()
for i in range( 2, 8 ):
    print( i, end='' )
    for j in range( 16 ):
        c = i*16+j
        print( ' '+chr( c ), end='' )
    print()
```

Ik prefereer het als je de functies `ord()` en `chr()` gebruikt in een
programma waar je de codes van tekens moet gebruiken. Als je wilt
refereren aan de code voor de letter `"A"`, schrijf dan niet 65, maar
schrijf in plaats daarvan `ord("A")`. 65 heeft alleen betekenis voor
mensen die ASCII codes van buiten kennen, en je programma zou
betekenisvol moeten zijn voor iedereen. Daarbovenop komt nog dat, hoewel
ASCII een zeer wijd verbreide standaard is, er nog steeds computers zijn
die andere manieren van het coderen van tekens gebruiken, dus de code
voor `"A"` is niet noodzakelijkerwijs 65 (inderdaad, IBM, ik heb het
over jou).

### UTF-8

Python ondersteunt Unicode, specifiek de meeste gebruikelijke versie van
Unicode, namelijk UTF-8. Dit betekent dat je allerhande "vreemde" tekens
kunt gebruiken. Ik legde uit bij de beschrijving van functie en
variabele namen dat je "letters" in die namen kunt gebruiken. Je nam
toen waarschijnlijk aan dat ik `"A"` tot en met `"Z"` en `"a"` tot en
met `"z"` bedoelde. Het grappige is dat het afhankelijk is van je
computersysteem wat daadwerkelijk beschouwd wordt als letter.
Bijvoorbeeld, als in je computer staat ingesteld dat de taal die je
gebruikt Duits is, dan kun je letters gebruiken met umlauts. Ook het
Nederlands heeft speciale letters. Ik raad je echter ten zeerste af dit
soort speciale letters te gebruiken in namen voor functies en
variabelen. Niet alleen zijn ze lastig te typen, maar ze maken ook je
programma minder goed overdraagbaar naar andere systemen.

In UTF-8 kun je in strings de reguliere tekens opnemen precies als je
zou verwachten. Je kunt ook speciale letters opnemen, maar die zien er
meestal anders uit dan je zou verwachten. Omdat Python UTF-8
ondersteunt, moet je voorzichtig zijn als je teksten kopieert van,
bijvoorbeeld, een tekstverwerker. Tekstverwerkers hebben de irritante
gewoonte om tekens te veranderen in andere tekens, bijvoorbeeld "rechte"
aanhalingstekens in "kromme," of een min-teken in een "dash." Als je
zulke tekens kopieert in je programma, zal Python de tekens accepteren,
maar zal ze dan niet beschouwen als, bijvoorbeeld, string begrenzingen.

Als je Unicode tekens in een string wilt opnemen, kun je dat doen met
Unicode codes. Je moet dan het UTF-8 nummer van het teken kennen dat je
wilt tonen. Je kunt dan de code `\uxxxx` opnemen, waarbij `xxxx` een
hexadecimaal getal van vier hexadecimale cijfers is, om het
corresponderende teken in de string te zetten. Bijvoorbeeld, de
onderstaande code toont het Griekse alfabet:[^14]

```python
alpha = "\u0391"
for i in range( 25 ):
    print( chr( ord( alpha )+i ), end=" " )
```

Over het algemeen hoef je je niet druk te maken over teken coderingen.
Ik raad je aan je te beperken tot ASCII waar mogelijk. Als je met
Unicode tekens moet werken, gaan de zaken meestal automatisch goed,
omdat Python Unicode ondersteunt. Af en toe zie ik vertalingsproblemen
als van Unicode naar ASCII moet worden gegaan, wat meestal te maken
heeft met bestandsverwerking. Het zal een tijdje duren voordat je dat
soort problemen krijgt, en ik zal er meer over zeggen in hoofdstuk
<a href="#ch:textfiles" data-reference-type="ref" data-reference="ch:textfiles">17</a>
en verder.

[^14]: Er staat een vreemd teken in deze reeks Griekse letters, namelijk
    tussen de Rho aen de Sigma, dat gelijk is aan `\u03A2`, dat
    klaarblijkelijk geen legaal Unicode teken is.
