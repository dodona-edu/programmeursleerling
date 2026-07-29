Schrijf een programma dat het omgekeerde is
van het vorige: nu neemt de gebruiker een getal in gedachten en de
computer probeert het te raden. Op de pogingen van de computer moet de
gebruiker antwoorden met een letter: "L" voor lager als het te raden
getal lager is, "H" voor hoger als het te raden getal hoger is, en "C"
voor correct (je kunt de `input()` functie hiervoor
gebruiken). Als de computer het getal geraden heeft, drukt het af
hoeveel pogingen er nodig waren. Zorg ervoor dat de computer ook herkent
dat er geen mogelijk antwoord is (misschien omdat de gebruiker een
vergissing heeft gemaakt, of omdat de gebruiker de computer in het ootje
probeerde te nemen). Een slim programma hoeft hoogstens tien keer te
raden.

### Opgave

De gebruiker neemt een getal tussen 1 en 1000 in gedachten (grenzen inbegrepen).
Tien pogingen volstaan enkel als de computer bij iedere gok het bereik van de
getallen die nog mogelijk zijn halveert. De computer houdt daarom het kleinste
en het grootste getal bij dat nog mogelijk is, en gokt altijd het midden van dat
bereik, naar beneden afgerond. De eerste gok is dus $$(1 + 1000) // 2 = 500$$.

Antwoordt de gebruiker `L`, dan wordt het grootste mogelijke getal de gok min
één. Antwoordt de gebruiker `H`, dan wordt het kleinste mogelijke getal de gok
plus één. Zodra het kleinste mogelijke getal groter wordt dan het grootste
mogelijke getal, is er geen enkel getal meer mogelijk en zegt de computer dat.

### Invoer

Eén regel met de letter `L`, `H` of `C` voor iedere gok van de computer.

### Uitvoer

Een regel `Is het g?` voor iedere poging, waarbij $$g$$ het getal is dat de
computer gokt. Nadat de gebruiker `C` geantwoord heeft, nog één laatste regel
`Aantal pogingen: n`, waarbij $$n$$ het aantal gokken is dat de computer nodig
had. Is er geen enkel getal meer mogelijk, dan luidt die laatste regel
`Dat is onmogelijk!`.

### Voorbeeld

In deze sessie had de gebruiker het getal 42 in gedachten.

#### Invoer:

```
L
L
L
L
H
L
H
C
```

#### Uitvoer:

```
Is het 500?
Is het 250?
Is het 125?
Is het 62?
Is het 31?
Is het 46?
Is het 38?
Is het 42?
Aantal pogingen: 8
```

### Voorbeeld

In deze sessie bleef de gebruiker antwoorden dat het te raden getal lager is,
waardoor er op het einde geen enkel getal meer mogelijk is.

#### Invoer:

```
L
L
L
L
L
L
L
L
L
```

#### Uitvoer:

```
Is het 500?
Is het 250?
Is het 125?
Is het 62?
Is het 31?
Is het 15?
Is het 7?
Is het 3?
Is het 1?
Dat is onmogelijk!
```
