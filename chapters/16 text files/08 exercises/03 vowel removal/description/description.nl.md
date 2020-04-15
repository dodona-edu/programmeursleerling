Schrijf een functie `zonder_klinkers` waaraan twee locaties van tekstbestanden (`str`) moeten doorgegeven worden. De functie moet de inhoud van het eerste tekstbestand kopiëren naar het tweede tekstbestand, maar waarbij alle klinkers verwijderd worden. De functie moet een tuple met twee elementen teruggeven: *i*) het totaal aantal karakters dat werd ingelezen uit het eerste tekstbestand en *ii*) het totaal aantal karakters dat werd uitgeschreven naar het tweede tekstbestand.

### Voorbeeld

In onderstaande interactieve sessie gaan we ervan uit dat het tekstbestand [`data.txt`](media/data/data.txt) zich in de huidige directory bevindt.

```console?lang=python&prompt=>>>
>>> print(open('data.txt', 'r').read(), end='')
How much wood would a woodchuck chuck
If a woodchuck could chuck wood?
He would chuck, he would, as much as he could,
And chuck as much as a woodchuck would
If a woodchuck could chuck wood.
>>> zonder_klinkers('data.txt', 'kopie.txt')
(190, 135)
>>> print(open('kopie.txt', 'r').read(), end='')
Hw mch wd wld  wdchck chck
f  wdchck cld chck wd?
H wld chck, h wld, s mch s h cld,
nd chck s mch s  wdchck wld
f  wdchck cld chck wd.
```
