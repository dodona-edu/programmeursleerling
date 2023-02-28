In veel opgaves in dit boek is het nuttig om een functie te hebben die
gebruiker een input laat geven die voldoet aan specifieke eisen. Ik heb
een module gecreëerd, `pcinput` geheten, die een aantal van die functies
bevat. In veel van de opgaves en voorbeelden in dit boek veronderstel ik
dat je die module beschikbaar hebt. Je kunt de module downloaden van
<http://www.spronck.net/pythonbook>{:target="_blank"}, of de code hieronder overnemen in
een bestand "pcinput.py," ervoor zorgend dat deze is opgeslagen in
dezelfde directory als waar je je eigen code schrijft.

Deze functies zijn wat lelijk omdat ze foutmeldingen geven als er iets
mis is. Maar mooiere functies zouden lastiger zijn om te gebruiken (je
moet dan exceptions afhandelen, en die behandel ik pas in hoofdstuk
18).
Om Python te leren zijn ze uitstekend geschikt.

Ieder van de functies vraagt de gebruiker om een waarde in te geven van
een bepaald type (float, integer, string, of hoofdletter), en
retourneert die waarde. Je kunt de functies aanroepen met een string als
argument, die dan als prompt gebruikt wordt.

```python
def getFloat( prompt ):
    while True:
        try:
            num = float( input( prompt ) )
        except ValueError:
            print( "Geen getal -- probeer het opnieuw" )
            continue
        return num

def getInteger( prompt ):
    while True:
        try:
            num = int( input( prompt ) )
        except ValueError:
            print( "Geen geheel getal -- probeer het opnieuw" )
            continue
        return num

def getString( prompt ):
    line = input( prompt )
    return line.strip()

def getLetter( prompt ):
    while True:
        line = input( prompt )
        line = line.strip()
        line = line.upper()
        if len( line ) != 1:
            print( "Geef precies een letter in" )
            continue
        if line < 'A' or line > 'Z':
            print( "Geef een letter van het alfabet in" )
            continue
        return line
```
