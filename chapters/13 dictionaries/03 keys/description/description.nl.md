Zoals ik aangaf kan ieder onveranderbaar data type een dictionary key
zijn. Dat betekent dat je strings, integers, en floats kunt gebruiken
als keys. Je herinnert je wellicht dat tuples ook onveranderbaar zijn,
wat betekent dat ook tuples als keys gebruikt kunnen worden. Dat is soms
nuttig.

Een eenvoudig voorbeeld van het nut van tuples als keys is een
dictionary waarbij je informatie wilt opslaan die geassocieerd is met
punten in een 2-dimensionale ruimte (ik besprak dit in hoofdstuk
12).
Er is geen goede manier waarmee je een 2-dimensionaal punt kunt opslaan
als een enkel getal of string. Het is niet onmogelijk (je kunt
bijvoorbeeld het getallenpaar omzetten naar hun string-representatie en
ze met een komma ertussen tot één string maken) maar het wordt al snel
verwarrend (bijvoorbeeld, de strings `"2,3"`, `"2, 3"`, `"+2,+3"`, en
`"02,03"` zouden alle dezelfde tuple representeren, terwijl het
verschillende keys zijn).
