Schrijf een boter-kaas-eieren programma dat
twee mensen het spel samen laat spelen. Om de beurt vraagt het programma
iedere speler om de rij en de kolom waar ze een teken willen plaatsen.
Zorg ervoor dat het programma alleen een rij/kolom combinatie toestaat
die binnen het bord valt en leeg is. Als een speler heeft gewonnen,
eindigt het spel. Als het bord vol is, eindigt het spel ook, met een
gelijkspel.

Dit is een redelijk lang programma om te schrijven (60 regels code of
zo). Gebruik maken van functies helpt. Ik raad je aan een functie
`toon\_bord()` te schrijven die het bord als parameter krijgt en die het
laat zien. Maak ook een functie `neemRijKolom()` die de gebruiker om een
rij/kolom combinatie vraagt en die controleert of het een legale invoer
betreft. Maak ook een functie `winnaar()` die controleert of het bord
een winnaar heeft. Houd bij wie aan de beurt is middels een variabele
`speler` in het hoofdprogramma, die je kunt meegeven aan een functie als
argument als de functie dit moet weten. Ikzelf bouw ook altijd een
functie `opponent()` die de speler als argument krijgt en de andere
speler teruggeeft; een dergelijke functie kan gemakkelijk gebruikt
worden om van speler te wisselen na een zet.

Het hoofdprogramma zal er ongeveer als volgt uitzien (in pseudo-code):

    toon bord
    while True:
        vraag om de rij
        vraag om de kolom
        if de rij/kolom combinatie al bezet is:
            geef een foutboodschap
            continue
        plaats een markering voor de speler op de rij/kolom
        toon bord
        if er is een winnaar:
            feliciteer winnaar
            break
        if bord is vol:
            zeg dat het gelijkspel is
            break
        wissel spelers
