Tot op dit moment heb ik alleen gesproken over het opslaan bij een key
in een dictionary van een enkele waarde van een enkel data type. Het is
echter ook mogelijk om complexe waardes op te slaan in een dictionary.
De waardes kunnen willekeurige Python objecten zijn. Bijvoorbeeld, je
kunt bij iedere key een list opslaan. Hieronder staat een dictionary
waarbij ik studenten opsla die een cursus volgen. De cursus wordt
geïdentificeerd door het cursusnummer. De studenten worden
geïdentificeerd door hun studentnummers.

```python
curses = {
    '880254':['u123456', 'u383213', 'u234178'], 
    '822177':['u123456', 'u223416', 'u234178'], 
    '822164':['u123456', 'u223416', 'u383213', 'u234178']}

for c in curses:
    print( c )
    for s in curses[c]:
        print( s, end=" " )
    print()
```

Stel je voor dat ik niet alleen de studentnummers per cursus wil
opslaan, maar ook de cursusnaam, de cursus ECTS (ECTS is een standaard
voor studiepunten), en voor iedere student een eindcijfer. Je kunt dat
(bijvoorbeeld) doen door als waarde bij een cursusnummer een dictionary
op te nemen, met drie keys: `"naam"`, `"ects"`, en `"studenten"`. De
waarde bij `"naam"` is de cursusnaam als een string, de waarde voor
`"ects"` is een integer, en de waarde voor `"studenten"` is een andere
dictionary, die studentnummers als keys gebruikt en eindcijfers als
waardes.

```python
curses = {
    '880254': 
    { "naam":"Onderzoeksvaardigheden Data Processing", "ects":3, 
        "studenten":{'u123456':8, 'u383213':7.5, 'u234178':6} }, 
    '822177': 
    { "naam":"Logica", "ects":6,
        "studenten":{'u123456':5, 'u223416':7, 'u234178':9} }, 
    '822164': 
    { "naam":"Computer Games", "ects":6,
        "studenten":{'u123456':7.5, 'u223416':9 } } }

for c in curses:
    print( "{}: {} ({})".format( c, curses[c]["naam"], 
        curses[c]["ects"] ) )
    for s in curses[c]["studenten"]:
        print( "{}: {}".format( s, curses[c]["studenten"][s] ) )
    print()
```

Data structuren kunnen nog complexer worden dan dit als je dat wilt.
Echter, als je inderdaad overweegt om Python programma's te maken voor
dit soort data structuren, doe je er goed aan om eerst object oriëntatie
te bestuderen (hoofdstuk
<a href="#ch:objectorientation" data-reference-type="ref" data-reference="ch:objectorientation">21</a>
en verder) en waarschijnlijk een aparte cursus over databases te volgen.
