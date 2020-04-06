Het maken van een module is eenvoudig. Je maakt gewoon een Python
bestand, met de extensie `.py`, en plaatst er de functies in die je in
de module wilt hebben. Je kunt dit Python bestand dan importeren in een
ander Python programma (je gebruikt gewoon de naam van het bestand
zonder de extensie `.py`; het bestand moet in dezelfde folder als het
programma staan, of in de folder waar Python altijd zoekt naar modules),
en je kunt de functies gebruiken op dezelfde manier als je functies uit
de reguliere Python modules gebruikt, dat wil zeggen, je kunt ofwel
specifieke functies uit de module importeren, ofwel de hele module
importeren en de functies gebruiken via de `<module>.<functie>()`
syntax.

### `main()`

Als je de code van andermans Python programma's bekijkt, zeker
programma's die functies bevatten die je mogelijk zou willen importeren,
zie je vaak een constructie als de volgende:

```python
def main():
    # code...
    
if __name__ == '__main__':
    main()
```

De functie `main()` bevat feitelijk het hoofdprogramma, dat andere
functies kan aanroepen.

Je hoeft dit niet precies te begrijpen, maar wat hier aan de hand is is
het volgende: het Python bestand bevat code die als programma kan
draaien, of de functies die het bevat kunnen geïmporteerd worden in
andere programma's. De bovenstaande constructie zorgt ervoor dat de code
in `main()` (dus het hoofdprogramma) alleen wordt uitgevoerd als het
programma als een separaat programma is gestart, en niet als een module
in een ander programma geladen is. Als in plaats daarvan het programma
als module is geladen, kunnen alleen de functies in het programma worden
geïmporteerd, en wordt de code voor `main()` genegeerd.

Een Python bestand dat een dergelijke constructie bevat en dat
voornamelijk als module wordt gebruikt, heeft vaak code in `main()` die
de functies test. Dat kan nuttig zijn tijdens de ontwikkeling van de
module.

Deze constructie heeft echter nog een tweede toepassing. Omdat `main()`
een functie is, hoef je als je het programma tussentijds wilt verlaten,
niet de `exit()` functie uit de `sys` module te gebruiken. In plaats
daarvan kun je gewoon `return` doen in de `main()` functie. Dit vermijdt
de lelijke foutboodschap die sommige editors geven bij gebruik van
`exit()`.
