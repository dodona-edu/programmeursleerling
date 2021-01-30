Zoals ik aan het begin van dit hoofdstuk aangaf, bestaan conditionele
statements, die ook wel "condities" of "`if` statements" worden genoemd
(omdat ze gedefinieerd worden met behulp van het gereserveerde woord
`if`), uit een test en één of meer acties, waarbij de acties alleen
worden uitgevoerd als de test `True` oplevert.

Hier is een voorbeeld:

```python
x = 5
if x == 5:
    print( "x is 5" )
```

De syntax van een `if` statement is als volgt:

```python
if <boolean expressie>:
    <acties>
```

Let op de dubbele punt (:) die achter de boolean expressie staat, en het
feit dat `<acties>` inspringt.

### Blokken code

In de syntactische beschrijving van de `if` statement, zie je dat
`<acties>` "inspringt," dus één tabulatie naar rechts is geplaatst (in
het Engels heet dit "indent"). Dit is opzettelijk zo gedaan en
noodzakelijk. Python beschouwt statements die elkaar opvolgen en die
hetzelfde niveau van inspringing hebben als één blok code. Het blok code
dat onder het `if` statement staat is de lijst van acties die worden
uitgevoerd als de boolean expressie `True` is. Bijvoorbeeld:

```python
x = 7
if x < 10:
    print( "Deze regel wordt alleen uitgevoerd als x < 10." )
    print( "En dat geldt ook voor deze regel." )
print( "Deze regel wordt echter altijd uitgevoerd." )
```

Wijzig de waarde van `x` en test hoe dat de resultaten beïnvloedt.

Dus alle regels code die onder de `if` staan en inspringen, horen tot
het blok code dat wordt uitgevoerd als de boolean expressie behorende
bij de `if` evalueert als `True`. Het blok code wordt daarentegen
overgeslagen als de boolean expressie evalueert als `False`. Statements
die volgen na de `if` en die niet inspringen (althans, niet zo diep als
het blok code onder de `if`) worden uitgevoerd ongeacht het resultaat
van de evaluatie van de boolean expressie.

Je hoeft je niet te beperken tot slechts één `if` statement. Je kunt er
zoveel hebben als je wilt.

```python
x = 5
if x == 5: 
    print( "x is 5" )
if x > 4: 
    print( "x is groter dan 4" )
if  x >= 5:
    print( "x is groter dan of gelijk aan 5" )
if x < 6: 
    print( "x is kleiner dan 6" ) 
if x <= 5:
    print( "x is kleiner dan of gelijk aan 5" )
if x != 6 :
    print( "x is niet 6" )
```

Wijzig weer de waarde van `x` en test hoe dat de resultaten beïnvloedt.

### Inspringen

**In Python is correct inspringen van het grootste belang!** Zonder
correcte inspringing kan Python niet zien welke regels code een blok
vormen, en kan daarom niet je code uitvoeren zoals je bedoelt.[^5]

Je kunt inspringen door middel van de `Tab` toets, of je kunt het doen
middels spaties. De meeste editors doen aan "auto-indenting," dat wil
zeggen, ze springen automatisch in als de code daartoe aanleiding geeft.
Bijvoorbeeld, als je een editor hebt die Python ondersteund, en je
schrijft een `if` statement, dan zal de editor de daarop volgende regel
meteen laten inspringen (als dat niet gebeurt, heb je waarschijnlijk een
syntax fout gemaakt, bijvoorbeeld de dubbele punt vergeten). Ook wordt
het niveau van inspringing aangehouden voor iedere volgende regel,
tenzij je middels de `Backspace` toets inspringing verwijdert.

In Python programma's is inspringing normaal vier spaties, dus een druk
op de `Tab` toets moet vier posities inspringen. Zolang je in een
specifieke editor werkt, kun je ofwel de `Tab` toets gebruiken, ofwel
zelf de spatiebalk vier keer indrukken, om één niveau van inspringing op
te schuiven. Je kunt echter in de problemen komen als je tussentijds
wisselt van editor, die wellicht andere instellingen voor tabulaties
gebruikt. Zelfs als je code in die andere editor er goed uitziet, kan
Python toch tijdens uitvoering melden dat er "indentation conflicts"
zijn (dat wil zeggen, dat tabulaties en spaties door elkaar gehutseld
zijn). Dat kan gezien worden als een syntax fout. De meeste editors
bieden de mogelijkheid via een optie om tabulaties automatisch te
vervangen door spaties, wat vermijdt dat zulke problemen optreden. Dus
als je een tekst editor gebruikt om Python code te schrijven, controleer
dan of die optie bestaat, en laat hem dan automatisch tabulaties
vervangen door vier spaties.

De volgende code bevat inspring-fouten. Verbeter de code.

```python
# Deze code bevat tabulatie-fouten!
x = 3
y = 4
if x == 3 and y == 4:
    print( "x is 3" )
   print( "y is 4" )
if x > 2 and y < 5:
print( "x > 2" )
print( "y < 5" )
if x < 4 and y > 3:
    print( "x < 4" )
        print( "y > 3" )
```

### Twee-weg beslissingen

Het komt regelmatig voor dat een beslissing twee kanten uit kan gaan,
dat wil zeggen, onder bepaalde omstandigheden wil je een bepaald iets
doen, en als die omstandigheden niet optreden wil je iets anders doen.
Python staat dit toe door aan een `if` statement een `else` tak toe te
voegen.

```python
x = 4
if x > 2:
    print( "x is groter dan 2" )
else:
    print( "x is kleiner dan of gelijk aan 2" ) 
```

De syntax is:

```python
if <boolean expressie>:
    <acties>
else:
    <acties>
```

Merk op dat er een dubbele punt achter de `else` staat, net zoals achter
de `<boolean expressie>` bij de `if`.

Het is van belang dat het woord `else` uitgelijnd is met het woord `if`
waar het bij hoort. Als je ze niet correct uitlijnt, krijg je ofwel een
tabulatie fout, ofwel je code doet niet wat je zou willen dat hij doet.

Een consequentie van het toevoegen van een `else` tak aan een `if`
statement is dat altijd precies één van de twee blokken `<acties>` wordt
uitgevoerd. Als de boolean expressie `True` is, wordt het blok code
onder de `if` uitgevoerd, en wordt het blok code onder de `else`
overgeslagen. Als de boolean expressie `False` is, wordt het blok code
onder de `if` overgeslagen, maar wordt het blok code onder de `else`
uitgevoerd.

![conditie](media/Condition.png "conditie"){:width="65%"}

Je kunt testen of een integer even of oneven is met de modulo operator.
Namelijk als `x % 2` nul is, dan is `x` even, en anders is `x` oneven.
Schrijf code die vraagt om een integer en dan rapporteert of de integer
even of oneven is (je kunt de `getInteger()` functie van `pcinput`
gebruiken om om een integer te vragen).

Opmerking met betrekking tot inspringing: het is niet absoluut
noodzakelijk om het blok code onder de `else` aan te lijnen met het blok
code onder de `if`, zolang de inspringing maar consistent is binnen het
blok code. Ervaren programmeurs gebruiken echter consistente inspringing
door de hele code, wat het gemakkelijk maakt om te zien hoe een
`if`-`else` statement werkt. Bijvoorbeeld, in de code hieronder is de
inspringing voor de `else` tak kleiner dan voor de `if` tak. Syntactisch
is dat correct, maar het maakt de code slechter leesbaar.

```python
# Syntactisch correct maar lelijke inspringing.
x = 1
if x > 2:
    print( "x is groter dan 2" )
else:
  print( "x is kleiner dan of gelijk aan 2" )
```

### Stroomdiagrammen

In de tijd dat het beroep "programmeur" nog vrij nieuw was, gebruikten
programmeurs vaak een techniek die "stroomdiagram" genoemd wordt om
algoritmes te beschrijven. Vandaag de dag worden stroomdiagrammen nog
slechts zelden gebruikt. Studenten hebben mij echter aangegeven dat
stroomdiagrammen helpen om begrip te krijgen van de exacte werking van
conditionele expressies (en van iteraties, die in het volgende hoofdstuk
besproken worden).

Een stroomdiagram is een schematische weergave van een algoritme middels
blokken met pijlen ertussen. Er zijn drie soorten blokken (althans, ik
heb voldoende aan drie soorten blokken voor dit boek). Rechthoekige
blokken bevatten statements die uitgevoerd worden. Ruitvormige blokken
bevatten een conditie die geëvalueerd wordt als `True` of `False`.
Rechthoekige blokken met ronde hoeken geven ofwel de start (met de tekst
"Start") ofwel het einde (met de tekst "Stop") van het algoritme aan.

Om een stroomdiagram te interpreteren, begin je bij het "Start" blok, en
volgt de pijlen, waarbij je ieder statement dat je tegenkomt uitvoert.
Als je een ruitvormig blok tegenkomt, evalueer je de conditie die erin
staat, en dan volg je ofwel de pijl die met `True` gemarkeerd is als de
conditie `True` is, ofwel de pijl die met `False` gemarkeerd is als de
conditie `False` is. Wanneer je het "Stop" blok tegenkomt, ben je klaar.

![twee-weg beslissing](media/Chart1.png "twee-weg beslissing"){:width="60%" data-caption="Stroomdiagram dat een twee-weg beslissing weergeeft."}

Bijvoorbeeld, de code die hierboven (in
<a href="#s:tweeweg" data-reference-type="ref" data-reference="s:tweeweg">[s:tweeweg]</a>)
staat, waarbij een getal vergeleken wordt met 2 en waarbij wordt
afgedrukt of het getal groter is dan 2, of kleiner dan of gelijk aan 2
is, is equivalent met het stroomdiagram dat getoond wordt in afbeelding
<a href="#f:chart1" data-reference-type="ref" data-reference="f:chart1">7.1</a>.

### Meer-weg beslissingen

Het komt voor dat je een situatie hebt waarbij je één van meerdere
blokken code wilt uitvoeren, maar niet meer dan één. Dit soort meer-weg
beslissingen kun je implementeren met een extra toevoeging aan een `if`
statement, namelijk in de vorm van één of meer `elif` takken (`elif`
staat voor "else if").

```python
leeftijd = 21
if leeftijd < 12:
    print( "Je bent een kind!" )
elif leeftijd < 18:
    print( "Je bent een teenager!" )
elif leeftijd < 30:
    print( "Je bent nog jong!" )
elif leeftijd < 50:
    print( "Beginnen grijze haren te komen?" )
else:
    print( "Wegen de jaren zwaar?" )
```

Deze code is equivalent aan het algoritme dat is weergeven in afbeelding
<a href="#f:chart2" data-reference-type="ref" data-reference="f:chart2">7.3</a>.

Verander in de code hierboven de waarde van de variabele `leeftijd` en
bestudeer de resultaten.

![meer-weg beslissing](media/Chart2nl.png "meer-weg beslissing"){:width="60%" data-caption="Stroomdiagram dat een meer-weg beslissing weergeeft."}

De syntax is:

```python
if <boolean expressie>:
    <acties>
elif <boolean expressie>:
    <acties>
else:
    <acties>
```

De syntax hierboven toont slechts één `elif`, maar je mag er meerdere
hebben. De verschillende tests in een `if`-`elif`-`else` constructie
worden in volgorde uitgevoerd. De eerste boolean expressie die
geëvalueerd wordt als `True` laat het bijbehorende blok code uitvoeren.
Geen andere blokken code in de hele constructie worden daarna nog
uitgevoerd, en er worden daarna ook geen boolean expressies in de
constructie meer getest.

Kortom, eerst wordt de boolean expressie bij de `if` geëvalueerd. Als
die `True` is, wordt het blok code onder de `if` uitgevoerd. Anders
wordt de boolean expressie bij de eerste `elif` geëvalueerd. Als die
`True` blijkt te zijn, wordt de code behorende bij deze `elif`
uitgevoerd. Zo niet, dan wordt de boolean expressie bij de tweede `elif`
geëvalueerd. Etcetera. Slechts als alle boolean expressies in de
constructie `False` blijken te zijn, wordt het blok code bij de `else`
uitgevoerd.

Voor het voorbeeld hierboven betekent dit dat bij de eerste `elif` de
test `leeftijd < 18` volstaat, en niet hoeft te worden aangevuld met een
test `and leeftijd >= 12`, want als `leeftijd` kleiner geweest zou zijn
dan 12, dan zou de boolean expressie voor de `if` al `True` zijn
geweest, en zou de boolean expressie bij de eerste `elif` niet eens door
Python zijn gezien.

Het toevoegen van `else` is altijd optioneel. In de meeste gevallen
waarin ik zelf meerdere `elif`s gebruik, zet ik wel een `else`, al was
het maar voor het afvangen van fouten.

Schrijf een programma dat een variabele `gewicht` heeft. Als `gewicht`
groter is dan $$20$$ (kilo), print je: "Er moet een toeslag van \$$25
betaald worden voor baggage die te zwaar is." Als `gewicht` kleiner is
dan $$20$$, print je: "Goede reis!" Als `gewicht` precies $$20$$ is, print
je: "Poeh! Dat gewicht is precies goed!" Wijzig de waarde van `gewicht`
een paar keer om de code te testen.

### Geneste condities

Gegeven de syntactische regels voor `if`-`elif`-`else` constructies en
inspringing, is het mogelijk om `if` statements op te nemen in de code
blokken behorende bij andere `if` statements. Zo'n geneste `if` wordt
alleen uitgevoerd als de boolean expressie behorende bij het code blok
waarin de geneste `if` staat `True` is.

```python
x = 41
if x%7 == 0:
    # --- Hier begint een genest blok code  ---
    if x%11 == 0:
        print( x, "is deelbaar door 7 en 11." )
    else:
        print( x, "is deelbaar door 7, maar niet door 11." )
    # --- Hier eindigt een genest blok code ---
elif x%11 == 0:
    print( x, "is deelbaar door 11, maar niet door 7." )
else:
    print( x, "is niet deelbaar door 7 of 11." )
```

Deze code is equivalent aan het algoritme dat wordt weergegeven in
afbeelding
<a href="#f:chart3" data-reference-type="ref" data-reference="f:chart3">7.4</a>.

Wijzig de waarde van `x` en controleer de resultaten.

In het voorbeeld hierboven wil ik alleen maar het nesten van `if`
statements demonstreren. Er zijn leesbaardere manieren om te doen wat
deze code doet. Het nesten van `if` statements kan vaak vermeden worden
door `elif`s te gebruiken. Bijvoorbeeld, de code hieronder doet
hetzelfde als de "leeftijd" code hierboven, maar nu met geneste `if`s in
plaats van `elif`s.

```python
leeftijd = 21
if leeftijd < 12:
    print( "Je bent een kind!" )
else:
    if leeftijd < 18:
        print( "Je bent een teenager!" )
    else:
        if leeftijd < 30:
            print( "Je bent nog jong!" )
        else:
            if leeftijd < 50:
                print( "Beginnen grijze haren te komen?" )
            else:
                print( "Wegen de jaren zwaar?" )
```

Ik neem aan dat je het ermee eens bent dat de versie met `elif`s
prettiger leest.

![geneste conditie](media/Chart3nl.png "geneste conditie"){:width="80%" data-caption="Stroomdiagram dat een geneste conditie weergeeft."}

[^5]: In veel programmeertalen (of eigenlijk in vrijwel alle
    programmeertalen) worden blokken code door de compiler/interpreter
    herkend doordat ze beginnen en eindigen met een speciaal symbool of
    gereserveerd woord. Bijvoorbeeld, in talen als Java en C++ worden
    blokken code omsloten door accolades, terwijl in talen als Pascal en
    Modula ze beginnen met het woord `begin` en eindigen met het woord
    `end`. Dat betekent dat in vrijwel alle talen correcte inspringing
    niet nodig is. Je ziet toch dat goede programmeurs correct
    inspringen, ongeacht de taal die ze gebruiken. Dat maakt het
    namelijk gemakkelijk te zien welke delen van de code bij elkaar
    horen, bijvoorbeeld, wat er hoort bij een `if` statement. Bij Python
    is het inspringen een verplichting. Voor ervaren programmeurs die
    voor het eerst Python leren komt dat wat vreemd over, maar ze
    beseffen al snel dat het ze niks uitmaakt – ze lieten hun code toch
    al netjes inspringen. Python maakt het echter ook voor beginnende
    programmeurs een noodzakelijkheid om netjes in te springen, wat
    betekent dat ze gedwongen zijn om nette code te schrijven. En dat is
    alleen maar nuttig voor iedereen.
