Creëer een programma dat de
gebruiker vraagt om getallen, totdat de gebruiker een nul ingeeft.
Daarna toont het programma het gemiddelde, de mediaan, en de modus van
de getallen. Je kunt de `statistics` module gebruiken voor het
gemiddelde en de mediaan; voor de modus toon je echter alle getallen die
het meest voorkomen, zelfs als dat betekent dat je meer dan één getal
moet tonen. Per definitie moet een getal dat modus is minstens twee keer
voorkomen; als ieder getal uniek is, is er geen modus. Hint: Je kunt de
`Counter` class gebruiken om de modus te construeren.

### Opgave

Schrijf een functie `modus` die een lijst van gehele getallen als argument neemt en een gesorteerde lijst teruggeeft van het getal (of de getallen) dat het vaakst voorkomt. Een getal telt enkel als modus als het minstens twee keer voorkomt; als ieder getal in de lijst maar één keer voorkomt, of als de lijst leeg is, is er geen modus en geeft de functie een lege lijst terug. Als meerdere getallen samen de hoogste telling hebben, geef je ze allemaal terug, gesorteerd van laag naar hoog.

Gebruik deze functie in je programma: blijf de gebruiker vragen om getallen totdat die een nul ingeeft, en toon dan het gemiddelde, de mediaan, en de modus van de ingegeven getallen (zonder de afsluitende nul mee te tellen). Je kunt de `statistics` module gebruiken voor het gemiddelde en de mediaan.

### Voorbeeld

```console?lang=python&prompt=>>>
>>> modus([4, 8, 15, 16, 23, 8, 4, 8])
[8]
>>> modus([7, 2, 9, 2, 9, 3])
[2, 9]
>>> modus([5, 10, 15])
[]
```
