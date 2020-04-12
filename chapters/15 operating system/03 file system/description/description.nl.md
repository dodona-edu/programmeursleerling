Het bestandssysteem (Engels: "file system") van een computer kun je zien
als een boomstructuur waarin directories en bestanden georganiseerd
zijn.

Er is een "root"[^19] directory, die het eerste toegangspunt is voor
alle andere directories. De root directory wordt geïdentificeerd door
een slash (`/`) of backslash (`\`), afhankelijk van het besturingssysteem.
Bij Windows is het de backslash, bij Mac OS en Linux is het de
voorwaartse slash. Windows ondersteunt tegenwoordig ook de voorwaartse
slash voor dit doel. Ik beveel aan dat je de voorwaartse slash gebruikt
indien mogelijk, omdat in strings de backslash gebruikt wordt om
speciale symbolen aan te geven. Dus als je in een string een de
backslash gebruikt om een directory scheider aan te geven, moet je een
dubbele backslash gebruiken. Dit is wat verwarrend, en daarom beveel ik
gebruik van de voorwaartse slash aan.

"Onder" de root-directory vind je meerdere andere directories, ieder met
een naam, en meestal ook meerdere bestanden, die ook ieder weer een naam
hebben. Onder iedere directory kun je weer andere directories en
bestanden vinden.

Ieder besturingssysteem legt bepaalde beperkingen op aan de namen van
directories en bestanden, hoewel over het algemeen de meeste tekens
gebruikt mogen worden. Het is de gewoonte dat reguliere bestanden een
extensie hebben, die aan het einde van de bestandsnaam wordt geplaatst,
en die van de bestandsnaam gescheiden is middels een punt. De extensie
geeft aan wat voor soort bestand het betreft, bijvoorbeeld, een
uitvoerbaar programma (`.exe`), een plat tekstbestand (`.txt`), of een
Python programma (`.py`). Het is ook de gewoonte dat directories geen
extensie hebben. Maar dit is geen verplichting, en je kunt zeker
bestanden aantreffen zonder, en directories met extensie. Merk op dat in
een visuele omgeving de extensies van bestanden vaak verborgen zijn,
maar ze zijn er wel – je ziet ze alleen niet.

Om een bestand uniek te identificeren, moet je het exacte "pad" vanaf de
root naar het bestand kennen, de directories volgend. Het pad van een
bestandsnaam ziet er uit als
`/<directory>/<directory>/…/<bestandsnaam>`. Bij Windows kan er nog de
letter van een disk drive voor het pad staan, waardoor het
`<drive>:/<directory>/<directory>/…/<bestandsnaam>` wordt.
Bijvoorbeeld, als je bij Windows op de "C" drive onder de root een
directory "Python34" hebt, waaronder je een directory "Lib" hebt, waarin
je een bestand "os.py" kunt vinden, dan is het pad voor dat bestand
`C:/Python34/Lib/os.py`. Bij Windows wordt er geen verschil gemaakt
tussen hoofd- en kleine letters, dus voor dit pad hadden ook alleen
kleine letters gebruikt mogen worden. Dat geldt echter niet voor alle
besturingssystemen.

Als je in een bestandssysteem werkt (en je werkt eigenlijk altijd in een
bestandssysteem, al realiseer je je dat misschien niet), dan is er een
"huidige directory," die geïdentificeerd wordt met een punt (`.`). Als
je een bestand in de huidige directory wilt benaderen, hoef je niet het
hele pad te kennen; dan is het genoeg als je alleen de bestandsnaam
kent. Eén directory "hoger" dan de huidige directory wordt
geïdentificeerd door twee punten (`..`). Boven de root zit de root zelf.

Tenslotte is het belangrijk te weten dat de meeste besturingssystemen
een manier hebben waarmee je bestanden kunt benaderen die niet in de
huidige directory staan, maar waarvan je het pad niet kent. Bij Windows
kun je bijvoorbeeld een `PATH` omgevingsvariabele zetten die alle
directories bevat die Windows doorzoekt als een uitvoerbaar bestand niet
in de huidige directory gevonden kan worden. Hoe je zo een
omgevingsvariabele een waarde moet geven voert echter te ver voor dit
boek.

[^19]: De "root" is de wortel van de boomstructuur, maar ik heb
    werkelijk nooit iemand dit "wortel" horen noemen.

