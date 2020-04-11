Alles wat je met bitsgewijze operatoren doet, kun je ook met de
gebruikelijke berekeningsmethodes doen, waarbij de gebruikelijke
methodes het voordeel hebben dat ze veel meer kunnen. Dus waarom zou je
bitsgewijze operatoren gebruiken?

Bitsgewijze operatoren werken ontzettend snel. Veel, veel sneller dan de
gebruikelijke methodes. Dus moet je ze gebruiken in berekeningen als dat
kan? Het antwoord is "nee," en wel om de volgende twee redenen:

-   Python is slim genoeg om te herkennen dat sommige berekeningen
    middels bitsgewijze operatoren kunnen worden uitgevoerd, en doet
    intern die conversie al voor je.

-   Als je echt verlegen zit om hele snelle code, kun je beter helemaal
    geen Python gebruiken.

Een andere reden die ik vaker genoemd hoor voor het gebruik van
bitsgewijze operatoren, is dat ze het mogelijk maken boolean waardes op
te slaan in een hele kleine data ruimte. Bijvoorbeeld, als ik acht
booleans moet opslaan kan ik dat doen in een tuple met die acht
booleans, wat minimaal acht bytes ruimte kost, of ik kan ze alle acht
opslaan in één byte middels bitsgewijze operatoren. Maar in de computers
van tegenwoordig is de besparing van ruimte niet erg belangrijk meer,
dus alleen als je spreekt over enorme data verzamelingen zou je je over
ruimte zorgen moeten gaan maken.

Dus wat is het nut van bitsgewijze operatoren? Als je het mij vraagt,
hebben ze erg weinig nut, tenzij je programma's moet maken die "dicht
tegen de machine" moeten werken. Soms zijn er data structuren die je het
beste met bitsgewijze operatoren kunt afhandelen. Bitsgewijze operatoren
kunnen ook zinvol zijn bij het manipuleren van binaire bestanden.

Om een voorbeeld te geven: kleuren zijn vaak gecodeerd in drie bytes,
namelijk een rood, een groen, en een blauw kanaal. Het nummer van een
kleur is dus een getal van drie bytes. Bitsgewijze operatoren zijn een
natuurlijke manier om de drie kanelen van elkaar te scheiden uit het
kleur-nummer. Hier is een functie die dat doet:

```python
def getRGB( color ):
    blauw = color & 255
    groen = (color >> 8) & 255
    rood = (color >> 16) & 255
    return rood, groen, blauw
    
r, g, b = getRGB( 223567 )
print( "rood={}, groen={}, blauw={}".format( r, g, b ) )
```

Voor iemand die met kleur-coderingen werkt, leest een dergelijke functie
erg natuurlijk.
