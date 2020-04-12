De `glob` module verschaft een functie `glob()` waarmee je een list van
bestandsnamen kunt produceren, gebaseerd op een zoek-patroon dat als
argument wordt meegegeven. Het zoek-patroon wordt geschreven volgens
Unix conventies, waarvan de meeste ook op andere systemen gelden. Deze
zijn als volgt:

-   Een vraagteken (`?`) in een bestandsnaam duidt op een willekeurig
    teken

-   Een ster (`*`) in een bestandnaam duidt op een sequentie van nul of
    meer willekeurige tekens

-   Een reeks van tekens tussen vierkante haken (`[]`) duidt op een
    willekeurig teken uit deze reeks; een streepje tussen twee van de
    tekens duidt op een reeks die begint bij het linkerteken en eindigt
    bij het rechterteken

Bijvoorbeeld, het patroon `"A[0-9]?B.*"` zoekt alle bestanden die
beginnen met de letter A, gevolgd door een cijfer, gevolgd door een
willekeurig teken, gevolgd door een B, met een willkeurige extensie. Het
hangt af van het besturingssysteem of dit patroon onderscheid maakt
tussen hoofd- en kleine letters.

Verwar een dergelijk patroon niet met een reguliere expressie.
Oppervlakkig gezien lijken ze op elkaar (zoals het feit dat een \* een
serie willekeurige tekens weergeeft), maar ze zijn compleet
verschillend. Dit soort bestand-zoek-patronen ondersteunen alleen de
speciale tekens en reeksen die hierboven staan (en die voor reguliere
expressies soms een andere betekenis hebben), en je gebruikt ze alleen
voor `glob` of wanneer je rechtstreeks met het besturingssysteem
communiceert in de command shell.

```python
from glob import glob

glist = glob( "*.pdf" )
for name in glist:
    print( name )
```

De `glob` module bevat ook een functie `iglob()`, waarvan de
functionaliteit gelijk is aan de functionaliteit van `glob()`, maar die
een iterator retourneert in plaats van een list.

Gebruik `glob()` om de namen van alle Python bestanden in de huidige
directory te tonen.

## `statistics`

De statistics module geeft je toegang tot diverse statistische functies.
Al deze functies krijgen als argument een sequentie of iterator met
getallen (integers of floats).

-   `mean()` berekent het gemiddelde van een sequentie van getallen

-   `median()` berekent de mediaan van een sequentie van getallen, dat
    wil zeggen, het "middelste" getal

-   `mode()` berekent de modus van een sequentie van getallen, dat wil
    zeggen, het getal dat het meest voorkomt

-   `stdev()` berekent de standaard deviatie van een sequentie van
    getallen

-   `variance()` berekent de variantie van een sequentie van getallen

Er zitten nog meer functies in de `statistics` module, maar de
bovengenoemde zijn het meest gebruikt. Voor geavanceerde statistische
berekeningen zijn andere modules beschikbaar, maar die noem ik niet in
dit boek.

Deze functies kunnen een `StatisticsError` genereren. Dit is relevant
voor de `mode()` functie, omdat deze exception gegenereerd wordt als er
geen unieke modus is.

```python
from statistics import mean, median, mode, stdev, variance, \
    StatisticsError

data = [ 4, 5, 1, 1, 2, 2, 2, 3, 3, 3 ]

print( "gemiddelde:", mean( data ) )
print( "mediaan:", median( data ) )
try:
    print( "modus:", mode( data ) )
except StatisticsError as e:
    print( e )
print( "st.dev.: {:.3f}".format( stdev( data ) ) )
print( "variantie: {:.3f}".format( variance( data ) ) )
```

Merk op dat voor een sequentie met een even aantal getallen, de mediaan
het gemiddelde is van de twee "middelste" getallen. Sommige mensen
prefereren een andere manier van omgaan met de mediaan bij een even
aantal getallen; als je een andere aanpak wilt, bestudeer dan andere
functies in de `statistics` module.

Wat betreft de modus: in de literatuur kun je verschillende definities
vinden van wat de modus is. De meest gebruikte definitie is "het meest
voorkomende getal," maar wat als er meerdere getallen zijn die alle het
meest voorkomen? Wat als ieder getal uniek is? De versie van de modus in
de `statistics` module lijkt niet de meest gebruikte te zijn.
