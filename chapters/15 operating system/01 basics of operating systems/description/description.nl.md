Een computer bestaat uit hardware, terwijl programma's bestaan uit
software. Software gebruikt de faciliteiten die de hardware biedt. Toen
computers voor het eerst geïntroduceerd werden, benaderden programmeurs
de hardware direct vanuit de programma's (bijvoorbeeld, om een pixel
zichtbaar te maken op het scherm, zette een programmeur een waarde in
een specifiek geheugenadres dat rechtstreeks aan het scherm gekoppeld
was – een praktijk die bekend stond onder de naam "poking"). Vandaag de
dag is de hardware zo complex en divers dat dit niet langer een
geschikte aanpak is. Laar staan het feit dat als je een programma wilt
schrijven dat op meerdere computers moet kunnen draaien, je het je niet
kunt veroorloven om hardware direct aan te spreken aangezien hardware
verschilt tussen computers. Daarom benaderen programma's de hardware
functionaliteiten via een "besturingssysteem."

Een besturingssysteem kan gezien worden als een laag tussen programma's
en hardware, die de programma's allerhande hoog-niveau functies biedt om
de hardware aan het werk te zetten. Typische besturingssystemen die
vandaag op thuiscomputers gebruikt worden zijn Microsoft's "Windows,"
Apple's "Mac OS," en het open-source besturingssysteem "Linux" (hoewel
er nog veel andere zijn). Ieder van deze systemen bestaat in meerdere
varianten, van elkaar onderscheiden door nummers of "builds," en soms
(bij Linux) door een bedrijfsnaam. Hoe dan ook, alle bieden
functionaliteiten om hardware aan te sturen.

Een probleem is dat hoewel alle besturingssystemen functionaliteiten
aanbieden, deze functionaliteiten niet op een consistente manier benoemd
zijn, en verschillen in parameter specificatie. Dit betekent dat als je
een Python programma wilt schrijven dat de hardware benadert door direct
met het besturingssysteem te communiceren, je programma niet kan draaien
op andere besturingssystemen. Dit is waar de `os` module een oplossing
biedt. De `os` module bevat functies die je kunt gebruiken om hardware
te benaderen, ongeacht het besturingssysteem. De `os` module heeft
daarom een verschillende implementatie voor verschillende
besturingssystemen, maar je programma hoeft dat niet te weten, omdat de
functies altijd dezelfde naam en dezelfde parameters hebben.

Dat betekent niet dat je helemaal niks hoeft te weten van de details van
een besturingssysteem. Bijvoorbeeld, als je een bestand benadert, moet
je bij Windows soms de letter toevoegen die een disk drive
identificeert, die niet bestaat bij Mac OS. Een ander verschil is dat
bestandstoegang en bestandsbeveiliging veel meer flexibiliteit heeft bij
Linux dan bij Windows of Mac OS, waardoor je bij Linux een ander soort
foutmeldingen kunt verwachten. Er zijn ook functies die weliswaar
bestaan voor alle besturingssystemen, maar die slechts bij sommige een
effect hebben. Desondanks is de `os` module een acceptabel compromis
tussen portabiliteit en besturingssysteem-afhankelijkheid.
