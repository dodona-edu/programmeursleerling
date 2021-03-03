Het concept "anonieme functies" mag je als optioneel materiaal
beschouwen: anonieme functies worden niet vaak gebruikt en zijn nooit
nodig. Maar om het verhaal over functies compleet te krijgen,
bediscussieer ik ze hier.

Python staat het toe om functies te creëren die geen naam hebben. De
functie kan aan een variabele toegekend worden, en je kunt die variabele
dan gebruiken alsof het een functie is. Je gebruikt hiervoor de volgende
syntax:

```python
lambda <parameters>: <actie>
```

`lambda` is een gereserveerd woord. `<parameters>` is een serie parameter
namen, van elkaar gescheiden middels komma's als er meer dan één is.
`<actie>` is één commando. De anonieme functie heeft geen `return`, maar
de waarde van `<actie>` wordt gebruikt als retourwaarde.

Bijvoorbeeld, de volgende code creëert een anonieme functie die het
kwadraat van de parameter berekent. De functie wordt toegekend aan de
variabele `f`. `f` kan dan worden gebruikt als functie om de kwadraten
van getallen te berekenen.

```python
f = lambda x: x*x
print( f(12) )
```

Deze code is exact gelijk aan de volgende code:

```python
def f( x ):
    return x*x
print( f(12) )
```

Dus anonieme functies zijn niet anders dan reguliere functies, maar
beperkter aangezien ze slechts kunnen bestaan uit een enkele regel code.
Waarom worden ze dan door Python ondersteund? Er is heel wat
gedebatteerd onder de mensen die Python ontwikkelen over de vraag of
`lambda` in de taal moet blijven. Het is ooit opgenomen in Python omdat
het ook zit in andere talen, specifieke in functionele programmeertalen
als Lisp en Haskell, die bestaan bij gratie van het concept van anonieme
functies. Maar `lambda` in Python is lang niet zo krachtig als `lambda`
in die andere talen, en, zoals ik liet zien, eigenlijk overbodig. De
voornaamste reden dat het nog steeds in Python zit is als restant van
het verleden en het belang dat de voorstanders van het gereserveerde
woord eraan hechten.

Af en toe hebben anonieme functies nut, omdat ze een programma iets
beter leesbaar kunnen maken. Ik toon hiervan een voorbeeld in hoofdstuk
<a href="#ch:lists" data-reference-type="ref" data-reference="ch:lists">13</a>.
