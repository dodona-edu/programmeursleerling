Ieder probleem dat optreedt bij het benaderen van een bestand, of het nu
het niet kunnen vinden van het bestand betreft, of de onmogelijkheid om
het bestand te lezen of the schrijven, of het doen van een poging om een
systeembestand of een directory te openen, leidt tot een `IOError`
exception. Omdat het niet ongebruikelijk is dat zulke problemen
optreden, en ze regelmatig niet door de programmeur voorzien kunnen
worden, is het een goed idee om `IOError` exceptions in je programma af
te vangen waar mogelijk.

Omdat er zoveel dingen fout kunnen gaan bij bestanden, kan de tuple
`args` die ik hierboven besprak gebruikt worden om meer informatie over
het probleem te krijgen. Bijvoorbeeld, als je programma aan de gebruiker
vraagt een bestandsnaam op te geven, en als je dan een `IOError` krijgt
als je het bestand probeert te openen, dan zou het error nummer (het
eerste element van de tuple) kunnen aangeven dat het bestand niet
bestaat (2). Een geschikte afhandeling zou dan zijn dat je de gebruiker
om een nieuwe bestandsnaam vraagt.

De error nummers zijn gedefinieerd in de `errno` module, die je in je
programma kunt importeren. De module geeft een aantal constanten die je
kunt opnemen in je code in plaats van getallen, en het is de gewoonte om
dat ook zo te doen. De meest voorkomende error nummers zijn:

-   `errno.ENOENT`: Dit bestand of deze directory bestaat niet. Dit
    krijg je als je een bestand benadert dat niet bestaat.

-   `errno.EACCESS`: Toestemming geweigerd. Je kunt deze melding in
    verschillende omstandigheden krijgen, zoals wanneer je probeert te
    lezen uit een gesloten bestand, of als je in een bestand probeert te
    schrijven dat voor alleen lezen bedoeld is, of als je een directory
    probeert te openen alsof het een bestand is.

-   `errno.ENOSPC`: Onvoldoende ruimte. Je krijgt deze fout als je een
    bestand probeert te schrijven en er geen ruimte voor het bestand
    beschikbaar is, bijvoorbeeld als je probeert te schrijven naar een
    USB-stick die vol is.

Er is een grote lijst met dit soort error nummers, die je kunt vinden in
Python handleidingen. Je snapt ze wellicht niet allemaal, en het is dan
ook zo dat een hoop ervan nogal archaïsch zijn en niet meer kunnen
voorkomen op moderne computers. Het beste kun je proberen om alle
`IOError`s af te vangen, en als je er een tegenkomt tijdens het
ontwikkelen van een programma, de argumenten af te drukken zodat je het
error nummer kent, en ook de foutboodschap. Je kunt dan opzoeken wat de
fout precies inhoudt, en hem in je programma afvangen als dat op een
zinvolle manier kan.

Maar net als met andere exceptions, kun je ook exceptions bij
bestandsmanipulatie beter vermijden dan afvangen. Er is geen enkele
reden dat je ooit een "bestand bestaat niet" fout zou mogen krijgen,
omdat je kunt testen of een bestand bestaat met de `exists()` en
`isfile()` functies uit de `os.path` module.

```python
import errno

try:
    fp = open( "GeenBestand" )
    fp.close()
except IOError as ex:
    if ex.args[0] == errno.ENOENT:
        print( "Bestand niet gevonden!" )
    else:
        print( ex.args[0], ex.args[1] )
```

{:class="callout callout-info"}
> #### Opmerking
> `FileNotFoundError` is een "subclass" (zie hoofdstuk <a href="#ch:inheritance" data-reference-type="ref" data-reference="ch:inheritance">23</a>) van `IOError`. Dit betekent dat het afvangen van `FileNotFoundError` equivalent is met het afvangen van `IOError` `as ex` en testen of `ex.args[0]` de waarde `errno.ENOENT` bevat.
