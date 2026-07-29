Schrijf een programma dat een toevalsgetal
neemt tussen 1 en 1000 (je kunt `randint()` daarvoor gebruiken). Het
programma vraagt de gebruiker het getal te raden. Na iedere poging van
de gebruiker zegt het programma "Lager" als het te raden getal lager is,
"Hoger" als het te raden getal hoger is, of "Je hebt het geraden!" als
het getal correct is. Het programma eindigt met afdrukken hoeveel
pogingen de gebruiker nodig had om het getal te raden. Voor
test-doeleinden kan het slim zijn om het te raden getal op het scherm te
laten zien, totdat je zeker weet dat het programma goed werkt.

{:class="callout callout-warning"}
> #### Opgelet
> Alleen de regels die hieronder beschreven staan mogen uitgeschreven worden. Als je tijdens het testen het te raden getal liet afdrukken, haal dat er dan weer uit voor je je oplossing indient.

### Invoer

Een reeks gokken, één geheel getal per regel. Het programma leest enkel gokken
tot het getal dat het genomen heeft geraden is, de resterende gokken worden dus
genegeerd.

### Uitvoer

Eén regel voor iedere gok die ingelezen werd:

- `Lager` als het te raden getal lager is dan de gok

- `Hoger` als het te raden getal hoger is dan de gok

- `Je hebt het geraden!` als de gok het te raden getal is

Na de juiste gok nog één laatste regel `Aantal pogingen: n`, waarbij $$n$$ het
aantal gokken is dat de gebruiker nodig had.

### Voorbeeld

In deze sessie had het programma het getal 42 genomen.

#### Invoer:

```
500
250
125
62
31
46
39
42
```

#### Uitvoer:

```
Lager
Lager
Lager
Lager
Hoger
Lager
Hoger
Je hebt het geraden!
Aantal pogingen: 8
```
