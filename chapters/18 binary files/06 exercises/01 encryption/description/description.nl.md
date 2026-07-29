Creëer een eenvoudig encryptie
programma. Open een bestand in binaire modus, en lees het byte voor byte
in. Tel 128 op bij iedere byte die een waarde kleiner dan 128 heeft, en
trek 128 af van iedere byte die een waarde groter dan 128 heeft.
Overschrijf de byte met de nieuwe waarde. Test het programma op een
kopie van een tekstbestand (zorg ervoor dat het een kopie is, want de
file wordt onherroepelijk gewijzigd). Test de inhoud van het aangepaste
bestand: dat moet een rommeltje zijn geworden. Maar als je het programma
een tweede keer draait, zou je het originele bestand terug moeten
krijgen. Zo niet, dan zit er een fout in je programma. Ben je niet blij
dat je met een kopie gewerkt hebt?


### Opgave

Schrijf een functie `encrypteer` waaraan de locatie van een bestand (`str`) moet doorgegeven worden. De functie moet het gegeven bestand in binaire modus inlezen, en elke byte van het bestand overschrijven met zijn geëncrypteerde waarde: bij elke byte kleiner dan 128 wordt 128 opgeteld, en van elke byte groter dan of gelijk aan 128 wordt 128 afgetrokken. De functie geeft niets terug.

Omdat de encryptie haar eigen inverse is, krijg je met een tweede oproep op hetzelfde bestand de originele inhoud van dat bestand terug.

### Voorbeeld

In onderstaande interactieve sessie gaan we ervan uit dat het tekstbestand [`data.txt`](media/data/data.txt){:target="_blank"} zich in de huidige directory bevindt.

```console?lang=python&prompt=>>>
>>> print(open('data.txt', 'r').read(), end='')
Hello, world!
>>> encrypteer('data.txt')
>>> open('data.txt', 'rb').read()
b'\xc8\xe5\xec\xec\xef\xac\xa0\xf7\xef\xf2\xec\xe4\xa1\x8a'
>>> encrypteer('data.txt')
>>> print(open('data.txt', 'r').read(), end='')
Hello, world!
```
