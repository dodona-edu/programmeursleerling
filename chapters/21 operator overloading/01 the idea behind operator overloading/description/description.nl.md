Als je Python programma's schrijft voor basale data types, dan gebruik
je operatoren als optellen, aftrekken, vermenigvuldigen, en delen, net
zoals operatoren voor het maken van vergelijkingen en allerlei andere
standaard functionaliteiten. Zulke interacties zijn niet gedefinieerd
voor classes die je zelf maakt, maar Python staat het wel toe dat je
definieert wat er moet gebeuren als een programmeur probeert een
operator toe te passen op één van jouw classes. Dit wordt "operator
overloading" genoemd.

Bijvoorbeeld, stel dat je een class definieert die een representatie is
van een quaternion.[^23] Je weet dat het optellen en vermenigvuldigen
van quaternionen goed gedefinieerde operaties zijn. Daarom zou je
wellicht willen definiëren wat er gebeurt als je twee van je
quaternionen met elkaar verbindt middels de $+$ operator. Python staat
je toe dat vast te leggen. Python staat je toe wat de $+$ operator doet
voor iedere willekeurige class die je implementeert.

Is dat niet geweldig? Nu kun je een class `Student` definiëren, en
ervoor zorgen dat als twee studenten met een $+$ bij elkaar worden
geteld, hun leeftijden bij elkaar worden opgeteld. Prachtig, niet?

Nee, dat is helemaal niet prachtig. Het is overduidelijk een zinloze
operatie om twee studenten op te tellen. Je kunt proberen te verzinnen
wat een natuurlijke interpretatie zou zijn van het optellen van
studenten, maar je zult de conclusie moeten trekken dat wat je ook
verzint, het zal altijd iets onlogisch zijn. Je moet niet proberen een
optelling te definiëren voor klassen waarbij de optelling niet op een
natuurlijke manier bestaat. Eén van de gevaren van het toepassen van
operator overloading is dat als je het op een onnadenkende manier doet,
je programmacode nonsens kan lijken.

Maar operator overloading kent krachtige toepassingen. In de rest van
dit hoofdstuk zal ik een aantal van die toepassingen introduceren. Er
zijn er meer dan ik noem, maar ik zal de meest gebruikelijke aan de orde
laten komen.

Overigens is operator overloading een typisch voorbeeld van
"polymorphisme," een concept dat een functie toestaat verschillende
resultaten te produceren op basis van de types van de argumenten.
Polymorphisme wordt vaak genoemd als een van de krachtige eigenschappen
van object oriëntatie.

[^23]: Quaternionen zijn een extensie van complexe getallen. Het zijn
    4-dimensionale getallen, met een reëel deel en drie imaginaire
    delen, die `i`, `j`, en `k` genoemd worden, met specifieke
    definities voor de vermenigvuldiging van ieder van deze delen. Ik ga
    geen details verstrekken, omdat ze niet belangrijk zijn voor dit
    boek (je kunt ze opzoeken als je geïnteresseerd bent). Ik wil ze
    slechts gebruiken als een voorbeeld van een type getallen dat niet
    standaard in Python is opgenomen.
