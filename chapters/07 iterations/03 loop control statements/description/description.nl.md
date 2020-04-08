Er zijn drie statements die je controle geven over de wijze waarop een
loop uitgevoerd wordt. Dit zijn `else`, `break`, en `continue`. Ze
werken met zowel `while` als `for` loops.

### `else`

Net als bij een `if` statement, kun je aan het einde van een loop een
`else` statement toevoegen. Het blok code bij de `else` wordt uitgevoerd
wanneer de loop eindigt, dus wanneer de boolean expressie voor de
`while` loop `False` is, of bij de `for` loop wanneer het laatste item
verwerkt is.

Hier is een voorbeeld van `else` bij de `while` loop:

```python
i = 0
while i < 5:
    print( i )
    i += 1
else:
    print( "De loop eindigt, i is nu", i )
print( "Klaar" )
```

Deze code is equivalent aan het stroomdiagram in afbeelding
<a href="#f:chart5" data-reference-type="ref" data-reference="f:chart5">8.3</a>.
Het stroomdiagram geeft je wellicht het idee dat het niet zinvol is een
`else` te gebruiken, maar het kan heel nuttig zijn in combinatie met een
`break` (die ik hierna bespreek).

![while else](media/Chart5nl.png "while else"){:width="65%" data-caption="Stroomdiagram van een `while` loop met een `else`."}

Hier is een voorbeeld van `else` bij de `for` loop:

```python
for fruit in ( "appel", "mango", "aardbei" ):
    print( fruit )
else:
    print( "De loop eindigt, fruit is nu", fruit )
print( "Klaar" )
```

Merk op dat nadat de `while` loop hierboven geëindigd is, de waarde van
`i` 5 is. De waarde van `fruit` na de `for` loop hierboven is het
laatste item verwerkt is, dus `"aardbei"`.

### `break` <span id="ss:break"
label="ss:break">\[ss:break\]</span>

Het `break` statement maakt het mogelijk een loop voortijdig af te
breken. Als Python een `break` tegenkomt, stopt het met het verwerken
van de loop, en keert niet terug bij de eerste regel van de loop. In
plaats daarvan gaat de verwerking verder met de eerste regel code na de
loop.

Om te zien wat het nut daarvan is, volgt hier een interessante oefening.
Ik zoek een getal dat start met een 1, en als je die 1 verplaatst naar
het einde van het getal, dan is het resultaat een getal dat drie keer zo
groot is als het originele getal. Bijvoorbeeld, als ik het getal 1867
neem, en ik verplaats de 1 van de start naar het einde, dan krijg ik
8671. Als 8671 drie keer 1867 zou zijn, dan is dat het antwoord dat ik
zoek. Maar dat is niet zo, dus 1867 is niet correct. De code om dit op
te lossen is vrij kort, en geeft het laagste getal dat het probleem
oplost:

```python
i = 1
while i <= 1000000:
    num1 = int( "1" + str( i ) )
    num2 = int( str( i ) + "1" )
    if num2 == 3 * num1:
        print( num2, "is drie keer", num1 )
        break
    i += 1
else:
    print( "Geen antwoord gevonden" )
```

Deze code is weergegeven in het stroomdiagram in afbeelding
<a href="#f:chart6" data-reference-type="ref" data-reference="f:chart6">8.4</a>.

![while break](media/Chart6nl.png "while break"){:width="65%" data-caption="Stroomdiagram van een `while` loop met een `break`."}

In dit voorbeeld zie je een goed gebruik van `break`. Omdat ik geen idee
heb van hoe groot het nummer is dat ik zoek, controleer ik er gewoon een
heleboel. Ik laat `i` oplopen tot 1000000. Ik weet natuurlijk niet of ik
het antwoord vind voordat `i` 1000000 heeft bereikt, maar ik moet ergens
een grens stellen, want misschien bestaat er wel helemaal geen getal dat
aan de eis voldoet, en ik wil geen eindeloze loop bouwen. Maar gedurende
het testen van getallen kan ik een onverwacht een antwoord vinden, en
als dat gebeurt, dan "break" ik uit de loop, want het heeft dan geen zin
meer om nog meer getallen te testen.

Het punt is dat ik een maximum van 1000000 heb gekozen niet omdat ik
weet dat ik een miljoen getallen moet doorzoeken. Ik heb geen idee hoe
vaak ik door de loop moet. Ik weet alleen dat als ik een antwoord vind,
ik klaar ben en de loop verder kan afbreken. Dat is precies de bedoeling
van de `break`.

Als ik een beetje mijn best doe kan ik er best voor zorgen dat de
boolean expressie de vergelijking voor me doet, via iets als
`while i < 1000000 and num1 \`= 3 \* num2!. Dit wordt wat ingewikkeld,
en ik moet ook `num1` en `num2` waardes geven voordat de loop start. Het
is in principe altijd mogelijk om het gebruik van `break` te vermijden.
Maar een `break` kan code beter leesbaar maken, zoals het doet in dit
geval.

Een `break` kan niet gebruikt worden buiten een loop. `break`s zijn
alleen gedefinieerd voor loops. (Ik zie vaak studenten proberen `break`
statements te gebruiken in condities die niet in een loop zitten, en dan
vreemd opkijken als ze een runtime error krijgen.)

Let op: als een `break` wordt uitgevoerd bij een loop die ook een `else`
heeft, dan wordt de code bij de `else` *niet* uitgevoerd. Ik maak
daarvan goed gebruik bij de code hierboven: de tekst die aangeeft dat
geen antwoord gevonden is, wordt alleen afgedrukt als er niet met een
`break` uit de loop wordt gesprongen.

De volgende code controleert een cijferlijst van een student. Als alle
cijfers 5.5 of hoger zijn, dan is de student geslaagd. Maar als er één
of meer cijfers lager dan 5.5 zijn, dan is de student gezakt. De
cijferlijst wordt verwerkt door een `for` loop.

```python
for cijfer in ( 8, 7.5, 9, 6, 6, 6, 5.5, 7, 5, 8, 7, 7.5 ):
    if cijfer < 5.5:
        print( "De student zakt!" )
        break
else:
    print( "De student slaagt!" )
```

Voer de code hierboven uit en zie dat de student zakt. Verwijder dan de
5 van de cijferlijst en zie dat de student nu slaagt. Bestudeer de code
totdat je hem snapt.

### `continue`

Als het statement `continue` in een blok code bij een loop wordt
aangetroffen, wordt onmiddellijk het uitvoeren van de huidige cyclus in
de loop beëindigd, en wordt teruggekeerd naar de eerste regel van de
loop. Voor een `while` loop betekent dat dat de boolean expressie
opnieuw geëvalueerd wordt, en voor een `for` loop betekent het dat het
volgende item van de collectie genomen en verwerkt wordt.

De volgende code drukt alle getallen tussen 1 en 100 af die niet door 2
of 3 gedeeld kunnen worden, en die niet eindigen op een 7 of 9.

```python
num = 0
while num < 100:
    num += 1
    if num%2 == 0:
        continue
    if num%3 == 0:
        continue
    if num%10 == 7:
        continue
    if num%10 == 9:
        continue
    print( num )
```

Deze code is ook weergegeven in het stroomdiagram in afbeelding
<a href="#f:chart7" data-reference-type="ref" data-reference="f:chart7">8.6</a>.

![while continue](media/Chart7.png "while continue"){:width="40%" data-caption="Stroomdiagram van een `while` loop met meerdere `continue`s."}

Ik weet niet wat het nut van deze lijst is, maar in ieder geval helpt
`continue` om de code te schrijven. In plaats van `continue` te
gebruiken was het ook mogelijk geweest een grote boolean expressie te
schrijven die bepaalt of een getal afgedrukt moet worden, maar dat zou
snel onleesbaar worden. Maar, net zoals geldt voor `break` statements,
`continue` statements kunnen altijd vermeden worden als je dat echt
wilt. Ze helpen echter om code begrijpbaar te houden.

Net als `break` statements, kun je `continue` statements alleen
gebruiken in loops.

Wees heel, heel voorzichtig met het gebruik van `continue` in een
`while` loop. De meeste `while` loops gebruiken een getal dat het aantal
cycli door de loop inperkt. Gewoonlijk wordt een dergelijk getal
verhoogd als laatste regel van het blok code bij de loop. Een `continue`
statement dat wordt uitgevoerd voordat die laatste regel bereikt is,
keert terug bij de boolean expressie zonder dan het getal verhoogd is.
Dat kan makkelijk leiden tot een eindeloze loop. Bijvoorbeeld:

```python
i = 0
while i < 10:
    if i == 5:
        continue
    i += 1
```

is een eindeloze loop!

Schrijf een programma dat een reeks getallen doorloopt via een `for`
loop. Als er een nul wordt aangetroffen in de lijst getallen, dan moet
het programma onmiddellijk eindigen, en alleen het woord "Klaar"
afdrukken (gebruik een `break` om dit te implementeren). Negatieve
getallen moeten overgeslagen worden (gebruik een `continue` om dit te
implementeren; ik weet dat het ook kan met een conditie, maar ik wil dat
je oefent met `continue`). Als er geen nul in de reeks getallen staat,
moet het programma de som van alle positieve getallen afdrukken (doe dit
met een `else`). Druk altijd "Klaar" af als het programma eindigt. Test
het programma met de reeks `( 12, 4, 3, 33, -2, -5, 7, 0, 22, 4 )`. Met
deze getallen moet het programma alleen "Klaar" afdrukken. Als je de nul
verwijdert, moet het programma 85 afdrukken (en "Klaar").
