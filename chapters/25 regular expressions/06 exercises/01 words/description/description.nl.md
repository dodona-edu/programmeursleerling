Een woord in een tekst wordt gedefinieerd als een zo lang mogelijke reeks letters. Alle karakters die geen letter zijn, worden dus beschouwd als scheidingstekens voor woorden.

### Opgave

Schrijf een functie `woorden_splitsen` waaraan de locatie van een tekstbestand (`str`) moet doorgegeven worden. De functie moet een lijst (`list`) teruggeven met de opeenvolgende woorden in het gegeven tekstbestand.

### Voorbeeld

In onderstaande interactieve sessie gaan we ervan uit dat het tekstbestand [`data.txt`](media/data/data.txt){:target="_blank"} zich in de huidige directory bevindt.

```console?lang=python&prompt=>>>
>>> woorden_splitsen('data.txt')
['Broadcast', 'by', 'the', 'BBC', 'between', 'and', 'Monty', 'Python', 's', 'Flying', 'Circus', 'was', 'conceived', 'written', 'and', 'performed', 'by', 'its', 'members', 'Graham', 'Chapman', 'John', 'Cleese', 'Terry', 'Gilliam', 'Eric', 'Idle', 'Terry', 'Jones', 'and', 'Michael', 'Palin']
```
