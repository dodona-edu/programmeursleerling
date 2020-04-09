Alle variabelen hebben een data type. In veel programmeertalen wordt het
data type van een variabele gespecificeerd op het moment dat de
variabele gecreëerd wordt. Bijvoorbeeld, in C++ zet je het type van een
variabele voor de variabele naam op het moment dat je de variabele
definieert, als volgt:

```python
int secs_per_week = 7 * 24 * 60 * 60;
```

Dit wordt “hard typing” genoemd.[^4] Hard typing heeft als voordeel dat
als je waarde in een variabele probeert te stoppen van het verkeerde
type, het programma een foutmelding kan geven. Dit vermijdt een aantal
vervelende problemen die kunnen optreden tijdens het schrijven of
uitvoeren van een programma.

In Python geef je niet een vast type aan een variabele, maar de
variabele heeft wel een type, namelijk het type van de waarde die erin
is opgeslagen. Dit betekent dat als een variabele een nieuwe waarde
krijgt, het type ook kan veranderen. Dit wordt “soft typing” genoemd.
(Nota bene: Ik ben persoonlijk van mening dat Python nog geschikter zou
zijn om beginnelingen programmeren te leren als het hard typing in
plaats van soft typing zou hebben, maar Guido van Rossum, de ontwerper
van Python, is het daar niet mee eens.)

De data types die je tot nu toe gezien hebt zijn integer, float, en
string. Je kunt het data type van een waarde of variabele zien met
behulp van de functie `type()`.

```python
a = 3
print( type( a ) )
a = 3.0
print( type( a ) )
a = "3.0"
print( type( a ) )
```

Omdat variabelen een type hebben, past het effect van operatoren die
tussen variabelen staan zich aan aan de types van de variabelen.
Bijvoorbeeld, in de code hieronder wordt de optelling ($$+$$) twee keer
gebruikt, en het effect verandert naar gelang de variabele types.

```python
a = 1
b = 4
c = "1"
d = "4"
print( a + b )
print( c + d )
```

Omdat `a` en `b` beide getallen zijn, is de $$+$$ in `a + b` de numerieke
optelling. Omdat `c` en `d` beide strings zijn, is de $$+$$ in `c + d` de
“concatenatie” (“vastplak”) operator.

Wat gebeurt er in de code hierboven als je `a + c` probeert te printen?
Als je het niet weet, probeer het dan.

Wat toont de code hieronder? Denk erover na, en voer dan de code uit.
Zorg dat je snapt wat er gebeurt.

```python
naam = "John Cleese"
print( "naam" )
```

Wjzig de code hierboven zodat de naam van een bekend lid van Monty
Python wordt getoond.
