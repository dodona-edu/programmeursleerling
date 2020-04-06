Waarom zou je functies willen creëren? Er zijn een hoop goede redenen:

-   Je hebt een bepaalde functionaliteit voor je code nodig die je
    onafhankelijk van de rest van je programma wilt ontwikkelen. Als je
    een dergelijke functionaliteit in een functie stopt, betekent dat
    dat je nadat de functie gebouwd en getest is, je de functionaliteit
    kunt gebruiken zonder er verder over na te denken.

-   Er is een bepaalde functionaliteit die je op meerdere plekken in je
    programma nodig hebt, en je kunt beter die functionaliteit in een
    functie stoppen die op meerdere plekken aangeroepen wordt, dan dat
    je de code naar al die plekken kopieert.

-   Je hebt een functionaliteit in je code nodig die je kunt aansturen
    middels parameters. Als je dergelijke functionaliteit in een functie
    stopt, worden de parameters duidelijker en wordt de code
    gemakkelijker te lezen en te onderhouden.

-   Je programma is te lang om de inhoud goed te blijven overzien. Door
    de code op te splitsen in functies blijf je veel langer grip houden
    op de inhoud en werking.

-   Je hebt een probleem dat je te lastig vindt om in één keer op te
    lossen. Je besluit het probleem op te splitsen in meerdere
    sub-problemen die je wel aankunt. Functies zijn een natuurlijke
    manier om een dergelijke aanpak vorm te geven.

-   Een programma dat diep geneste condities of loops bevat, wordt veel
    leesbaarder als dieper geneste gedeeltes in een functie geplaatst
    worden.

-   Het hergebruik van code wordt goed gefaciliteerd door delen van code
    in functies te plaatsen.

-   Code die beschikbaar gesteld moet worden aan andere programmeurs,
    kan verspreid worden door gedocumenteerde functies in modules te
    plaatsen.

Over het algemeen gesproken, kunnen de voordelen van functies worden
samengevat als een middel om de volgende zaken te bewerkstelligen:

-   *Encapsulatie*: Het "inpakken" van een nuttig stuk code op zo'n
    manier dat het gebruikt kan worden zonder kennis van de specifieke
    werking van de code

-   *Generalisatie*: Het geschikt maken van een stuk code voor diverse
    situaties door gebruik te maken van parameters

-   *Beheersbaarheid*: Het verdelen van een complex programma in
    gemakkelijk-te-bevatten delen

-   *Onderhoudbaarheid*: Het gebruik maken van betekenisvolle
    functienamen en logische opdelingen om een programma beter leesbaar
    en begrijpbaar te maken

-   *Herbruikbaarheid*: Het faciliteren van de overdraagbaarheid van
    code tussen programma's

-   *Recursie*: Het beschikbaar maken van een techniek die "recursie"
    heet, wat het onderwerp is van hoofdstuk
    <a href="#ch:recursion" data-reference-type="ref" data-reference="ch:recursion">10</a>.
