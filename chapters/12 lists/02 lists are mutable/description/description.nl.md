Omdat lists veranderbaar (Engels: "mutable") zijn, mag je de inhoud van
een list wijzigen.

Om een element van de list te overschrijven, kun je er een nieuwe waarde
aan toekennen middels een assignment.

```python
fruitlist = ["appel", "banaan", "kers", "doerian", "mango"]
print( fruitlist )
fruitlist[2] = "aardbei"
print( fruitlist )
```

Je kunt ook een sub-list overschrijven door een nieuw list toe te kennen
aan de sub-list. De sub-list en de nieuwe list hoeven niet dezelfde
lengte te hebben.

```python
fruitlist = ["appel", "banaan", "kers", "doerian", "mango"]
print( fruitlist )
fruitlist[1:3] = ["framboos", "aardbei", "aalbes"]
print( fruitlist )
```

Je kunt nieuwe elementen aan een list toevoegen door ze toe te kennen
aan een lege sub-list.

```python
fruitlist = ["appel", "banaan", "kers", "doerian", "mango"]
print( fruitlist )
fruitlist[1:1] = ["framboos", "aardbei", "aalbes"]
print( fruitlist )
```

Je kunt elementen van een list verwijderen door een lege list aan de te
verwijderen sub-list toe te kennen.

```python
fruitlist = ["appel", "banaan", "kers", "doerian", "mango"]
print( fruitlist )
fruitlist[1:3] = []
print( fruitlist )
```

Door sub-lists en assignments te gebruiken, kun je lists aanpassen op
iedere manier die je wilt. Het is echter eenvoudiger om lists aan te
passen via methodes. Er zijn allerlei handige methodes beschikbaar, die
ik hieronder bespreek.

Neem een list die alleen woorden bevat (bijvoorbeeld één van de
`fruitlist`s hierboven). Verander ieder woord in de list in een woord
dat alleen uit hoofdletters bestaat. Op dit punt in het boek doe je dat
met behulp van een `while` loop die een variabele `i` laat starten bij 0
en laat oplopen tot `len(<``list``>)-1`. Gebruik `i` als index voor de
list.
