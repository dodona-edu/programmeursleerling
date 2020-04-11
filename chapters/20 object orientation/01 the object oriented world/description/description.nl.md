Ik typ dit terwijl ik zit aan mijn keukentafel. Naast mij staat een
fruitschaal. In de schaal liggen appels. Deze appels delen bepaalde
eigenschappen, maar hebben ook verschillen. Ze delen hun naam, hun
prijs, en hun leeftijd, maar ze hebben alle (iets) verschillende
gewichten. Op de schaal liggen ook peren. Net als de appels zijn ze een
soort fruit, maar ze hebben ook een hoop verschillen met appels:
verschillende namen, verschillende kleuren, verschillende bomen waar ze
aan groeien. Toch delen ze ook dingen met appels die alle fruitsoorten
delen, en waarin ze verschillen van, bijvoorbeeld, de tafel waar ik aan
zit. Bijvoorbeeld, ik kan appels eten, en ik kan ook peren eten. Maar ik
ga niet proberen een tafel te eten.

Als ik probeer mijn wereld te modelleren in een computerprogramma, moet
ik objecten modelleren: objecten als appels, peren, en tafels. Sommige
van die objecten hebben een hoop zaken gemeen, bijvoorbeeld, iedere
appel deelt veel eigenschappen met iedere andere appel. Het klinkt
daarom zinvol om een klasse "appel" te definiëren, die de eigenschappen
bevat die alle appels delen, en dan voor iedere individuele appel alleen
die eigenschappen in te vullen waarin ze verschillen van alle andere
appels. Hetzelfde kan ik doen voor peren, die hun eigen klasse "peer"
moeten krijgen. En hoewel "appels" en "peren" van elkaar verschillen,
delen ze ook eigenschappen die mij het gevoel geven dat ik ze een
gedeelde klasse moet geven: de klasse "fruit." Ieder object dat
thuishoort in de klasse fruit heeft in ieder geval de eigenschap dat ik
het kan eten. Wat betekent dat iedere appel niet alleen behoort tot de
klasse "appel," maar ook tot de klasse "fruit" – net als de "peren."

Als ik er goed over nadenk: ik kan meer eten dan alleen appels en peren.
Ik kan ook taart eten. En champignons. En brood. En drop. Dus misschien
heb ik nog een andere klasse nodig, waartoe ook de klasse "fruit"
behoort. De klasse "voedsel," misschien?

Waart dit toe leidt, is dat als ik probeer de wereld (of een deel ervan)
te modelleren, ik objecten moet modelleren – en in plaats van ieder
object apart te modelleren, kan ik beter klassen van objecten
definiëren, zodat ik generieke uitspraken kan doen over groepen
objecten. Ik kan spreken over relaties tussen klassen, en ik kan
functies definiëren die op klassen werken; bijvoorbeeld, ik kan een
functionaliteit "eten" definiëren die op ieder object werkt dat behoort
tot de klasse "voedsel," en die tot gevolg heeft dat het object
verwijderd wordt uit de wereld en dat de "voedingsstoffen" van het
object toekent aan de "eter." Omdat ik objecten kan eten als ze horen
tot de klasse "voedsel," kan ik "fruit" eten. En omdat ik "fruit" kan
eten, kan ik objecten eten die tot de klasse "appel" behoren.

In essentie is een computerprogramma een model van een deel van de
wereld. En als zodanig profiteren veel programma's van de mogelijkheid
om te kunnen werken met objecten, klassen, relaties, en
functionaliteiten (methodes) die werken met objecten.

### Studenten, docenten, en cursussen

Veel programma's moeten omgaan met personen. De studentenadministratie
moet omgaan met studenten, die personen zijn. De studenten volgen
cursussen, die gedoceerd worden door docenten, die ook personen zijn.
Ongetwijfeld slaat de administratie gegevens op over studenten en
docenten, en je mag veronderstellen dat de programmeur die de
studentenadministratie heeft geïmplementeerd slim genoeg was om een
enkele interface te gebruiken om de gegevens van personen in te voeren.

Wat voor data wordt door alle personen gedeeld, voor zover het de
studentenadministratie aangaat? Waarschijnlijk hebben alle personen een
voornaam en een achternaam. Ze hebben ook een adres. Ze hebben ook een
leeftijd en een geslacht. Om ze uniek te maken, geeft de
studentenadministratie iedere persoon een administratienummer (ANR).
Deze data elementen zijn alle "eigenschappen" of "attributen" van
"personen."

Ik noemde als eigenschappen voornaam, achternaam, adres, leeftijd,
geslacht, en administratienummer. Eén van deze eigenschappen is
eigenlijk meer een functie dan een eigenschap. Zie je welke?

Het antwoord is "leeftijd." Leeftijd wordt berekend middels de
geboortedatum en de huidige datum. Je kunt leeftijd voorstellen als
eigenschap, maar het is een eigenschap die iedere keer opnieuw berekend
moet worden als je hem nodig hebt. Je kunt hem niet als een vaste waarde
opslaan, omdat hij morgen anders kan zijn dan vandaag, terwijl alleen de
datum is veranderd. Als ik een klasse `Persoon` ontwerp die een persoon
modelleert, kan ik daarom het beste "geboortedatum" een eigenschap
maken, terwijl ik "leeftijd" implementeer als methode. Zoals je je
wellicht herinnert is een methode een functie die behoort bij een zeker
data type: als een data type `Persoon` gedefinieerd is, is
`geboortedatum` een attribuut van dat data type, terwijl `leeftijd()`
een methode is van het data type die de leeftijd van de persoon
retourneert als integer.

Studenten en docenten zijn allebei personen. Ze delen de eigenschappen
van de klasse `Persoon`. Toch zijn er verschillen. Docenten krijgen
bijvoorbeeld een salaris, maar studenten niet. Studenten kunnen
daarentegen cijfers krijgen voor cursussen, maar docenten niet; zij
doceren de cursussen. Hieruit kan ik de volgende twee zaken afleiden:

-   Hoewel studenten en docenten beide personen zijn, hebben ze
    duidelijke verschillen; daarom heb ik naast de klasse `Persoon` ook
    een klasse `Student` en een klasse `Docent` nodig, die beide worden
    afgeleid van de klasse `Persoon`.

-   "Cursussen" lijken een inherent onderdeel te zijn van de wereld van
    de studentenadministratie, dus wellicht heb ik ook een klasse
    `Cursus` nodig.

Als ik van `Cursus` een klasse heb gemaakt, worden relaties duidelijk.
Studenten hebben een relatie met meerdere cursussen, en docenten ook,
maar op een andere manier. Studenten "schrijven zich in" voor cursussen.
Het lijkt er dus op dat er een methode `inschrijven()` moet komen, die
ervoor zorgt dat een student een relatie krijgt met een cursus. De vraag
is: moet `inschrijven()` een methode zijn van `Student`, met de cursus
als argument, of een methode van `Cursus`, met de student als argument?
Wat denk je?

Het antwoord is: "dat hangt ervan af." Het hangt ervan af hoe je de
student beziet in het licht van de studentenadministratie. Voor mij als
docent voelt het natuurlijk aan om `inschrijven()` een methode te maken
van een cursus, omdat ik een cursus zie als een verzameling studenten.
Maar er is niks op tegen om een student te bezien als een entiteit die
een verzameling cursussen bevat. Je kunt er ook voor kiezen om
`inschrijven()` als een methode van zowel studenten als cursussen te
zien, of een andere klasse te definiëren die de methode `inschrijven()`
bevat met zowel de student als de cursus als argumenten.

Dit illustreert hoe moeilijk de object georiënteerde visie op
programmaontwerp kan zijn: door de klassen te definiëren die de wereld
modelleren waarmee het programma werkt, moet je keuzes maken die een
grote invloed hebben op de exacte aanpak van het programma. Zwakke
keuzes leiden tot implementatieproblemen. Je moet flink wat tijd
besteden aan het ontwerpen van het object georiënteerde model dat de
basis vormt voor het programma, en alle consequenties van je keuzes
proberen te overzien. Zelfs voor doorgewinterde programmeurs is dat een
moeilijke taak. Maar een solide object-georiënteerd model maakt
programma's gemakkelijk te lezen, te begrijpen, en te onderhouden. Het
object georiënteerde paradigma is vaak de moeite waard.

### Klassen, objecten, en hierarchiën

In de object-georiënteerde wereld behoort iedere onderscheidbare
entiteit tot een klasse (Engels: "class"). Een klasse is een generiek
model voor een groep entiteiten. De klasse beschrijft alle attributen
die de entiteiten gemeen hebben, en beschrijft de methodes die de klasse
aanbiedt waarmee de wereld buiten de klasse invloed op de klasse kan
uitoefenen.

Op zichzelf is een klasse geen entiteit. Een entiteit die behoort tot
een klasse, wordt een "object" genoemd. De terminologie is dat een
object een "instantie" (soms: "instantiatie," maar dat is geen correct
Nederlands) is van een bepaalde klasse. Een klasse beschrijft
attributen, maar een object dat een instantie is van de klasse geeft
waardes aan de attributen. En hoewel een klasse de methodes beschrijft
die hij ondersteunt, kun je een methode alleen uitvoeren voor een object
dat een instantie is van de klasse.

Een klasse is een data type, een object is een waarde.

Klassen bestaan in hierarchiën. Een generieke, hoog-niveau klasse kan
eigenschappen en methodes beschrijven die gedeeld worden door
verschillende sub-klassen. Een sub-klasse kan eigenschappen en methodes
toevoegen, en kan zelfs eigenschappen en methodes wijzigen (maar kan
over het algemeen niet eigenschappen of methodes verwijderen, en moet
dat ook nooit doen). Iedere sub-klasse kan zelf ook weer sub-klassen
hebben.

Bijvoorbeeld, de klasse `Appel` kan een sub-klasse zijn van de klasse
`Fruit`, die weer een sub-klasse kan zijn van de klasse `Voedsel`. Dit
betekent dat waar je in een programma een object nodig hebt dat een
instantie is van de klasse `Voedsel`, je niet alleen objecten mag
gebruiken die directe instanties van `Voedsel` zijn, maar ook objecten
die een instantie zijn van `Fruit` of van `Appel`. Dat werkt niet
andersom: als je bijvoorbeeld een functie hebt geschreven die een object
van de klasse `Appel` nodig heeft, kun je die niet gebruiken met
instanties van `Fruit`, of instanties van andere sub-klassen van
`Fruit`. Hoewel een `Appel` `Fruit` is, is `Fruit` geen `Appel`. Je kunt
geen `Appel`s met `Peer`en vergelijken.

Een klasse hiërarchie wordt geïmplementeerd met behulp van een
mechanisme dat "inheritance" ("overerving") wordt genoemd, wat het
onderwerp is van hoofdstuk
<a href="#ch:inheritance" data-reference-type="ref" data-reference="ch:inheritance">23</a>.

### Klassen en data types in Python

De meeste object-georiënteerde programmeertalen kennen een aantal basale
data types, en staan je toe om klassen te definiëren, wat neerkomt op
het definiëren van nieuwe data types. Dit gold ook voor Python tot en
met versie 2. Sinds Python 3 is echter ieder data type een klasse.

Je kunt dit deels zien aan de manier waarop een groot aantal
functionaliteiten van basale data types in Python geïmplementeerd zijn
als methodes. Een methode wordt altijd aangeroepen via de syntax
`<variabele>.<methode>()`, in tegenstelling tot functies, die worden
aangeroepen als `<functie>( <variabele> )`. Het feit, bijvoorbeeld, dat
als je een kleine-letter-versie van een string wilt creëren, je dit
effectueert middels `<string>.lower()` geeft al aan dat een string een
instantie van een klasse is.

Maar niet alleen strings zijn instanties van klassen: integers en floats
zijn dat ook. Ze hebben zelfs methodes, maar die worden zelden expliciet
aangeroepen. Methodes worden vaak wel impliciet aangeroepen,
bijvoorbeeld, als je twee getallen optelt met $+$, is dat eigenlijk de
aanroep van een methode. Ik zal dit bediscussiëren in hoofdstuk
<a href="#ch:operatoroverloading" data-reference-type="ref" data-reference="ch:operatoroverloading">22</a>.
