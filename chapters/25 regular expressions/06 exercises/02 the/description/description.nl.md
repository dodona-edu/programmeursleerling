Vind alle voorkomens van het woord "de" in een gegeven tekst.

### Opgave

Schrijf een functie `zoek_de_de` waaraan de locatie van een tekstbestand (`str`) moet doorgegeven worden. De functie moet een lijst (`list`) teruggeven met alle voorkomens van "de" als een afzonderlijk woord in het gegeven tekstbestand. Hierbij mag geen onderscheid gemaakt worden tussen hoofdletters en kleine letters. Zorg ervoor dat je de
combinatie "de" niet telt als het een onderdeel is van een ander woord
(bijvoorbeeld "onderdeel," "delicaat" of "woede").

### Voorbeeld

In onderstaande interactieve sessie gaan we ervan uit dat het tekstbestand [`data.nl.txt`](media/data/data.nl.txt){:target="_blank"} zich in de huidige directory bevindt.

```console?lang=python&prompt=>>>
>>> woorden_splitsen('data.nl.txt')
['Monty', 'Python', 's', 'Flying', 'Circus', 'werd', 'uitgezonden', 'door', 'de', 'BBC', 'tussen', 'en', 'en', 'werd', 'bedacht', 'geschreven', 'en', 'uitgevoerd', 'door', 'haar', 'leden', 'Graham', 'Chapman', 'John', 'Cleese', 'Terry', 'Gilliam', 'Eric', 'Idle', 'Terry', 'Jones', 'en', 'Michael', 'Palin']
```
