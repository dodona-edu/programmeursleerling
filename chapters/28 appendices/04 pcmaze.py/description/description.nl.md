In hoofdstuk
10
laat ik in een voorbeeld een doolhof doorzoeken. In dat voorbeeld
gebruik ik een module `pcmaze`, die ik voor dit boek heb geschreven. De
module bevat een doolhof, en geeft functies om eigenschappen van het
doolhof op te vragen. Je kunt de module downloaden van
<http://www.spronck.net/pythonbook>{:target="_blank"}, of de code hieronder overnemen in
een bestand "pcmaze.py," ervoor zorgend dat het in dezelfde directory
staat als waar je je eigen code schrijft.

```python
def connected( x, y ):
    if x > y:
        return connected( y, x )
    if (x,y) in ((1,5),(2,3),(3,7),(4,8),(5,6),(5,9),(6,7),
        (8,12),(9,10),(9,13),(10,11),(10,14),(11,12),(11,15),
        (15,16)):
        return True
    return False

def entrance():
    return 1

def exit():
    return 16
```
