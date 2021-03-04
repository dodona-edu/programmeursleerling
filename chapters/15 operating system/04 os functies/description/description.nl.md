De `os` module ondersteunt veel functies waarmee je het bestandssysteem
kunt beïnvloeden. Ik noem er slechts een paar, omdat veel functies een
beetje gevaarlijk zijn om te gebruiken (je kunt bijvoorbeeld gemakkelijk
per ongeluk bestanden verwijderen die je had willen houden), en je hebt
er ook niet zoveel nodig. Als je echt geïnteresseerd bent om het
bestandssysteem te manipuleren, kun je zelf de vele functies van de `os`
module bestuderen via de Python handleiding.

### `getcwd()`

`getcwd()` ("cwd" staat voor "current working directory") retourneert de
huidige directory als een string.

```python
from os import getcwd
print( getcwd() )
```

### `chdir()`

`chdir()` wijzigt de huidige directory. De nieuwe directory geef je mee
als string argument.

```python
from os import getcwd, chdir

home = getcwd()
print( home )
chdir( ".." )
print( getcwd() )
chdir( home )
print( getcwd() )
```

### `listdir()`

`listdir()` retourneert een list die alle bestanden en directories bevat
in de directory die als argument is meegegeven. De namen verschijnen in
willekeurige volgorde. Ze bevatten niet het volledige pad.

```python
from os import listdir

flist = listdir( "." )
for naam in flist:
    print( naam )
```

### `system()`

`system()` krijgt een string argument dat beschouwd wordt als
systeemcommando, dat door Python wordt uitgevoerd in de command shell.
Je kunt de functie te gebruiken om alles te doen wat door het
besturingssysteem ondersteund wordt, inclusief het opstarten van andere
programma's. Er zijn echter betere manieren om andere programma's te
starten (zoek maar naar functies waarvan de naam begint met "exec").
