Er bestaan verschillende versies van Python. De meest populaire versies
zijn Python 2 en Python 3. Python 3 is, zoals je kunt verwachten, een
update van Python 2. Python 2 programma's zijn helaas niet volledig
compatibel met Python 3 (met andere woorden, je kunt Python 2
programma's over het algemeen niet draaien op een computer waarop je
alleen Python 3 geïnstalleerd hebt). Omdat er nog steeds een hoop Python
2 programma's gebruikt worden, is Python 2 een taal die nog steeds
onderhouden wordt.

Python 3 is gemaakt om een aantal inconsistenties en eigenaardigheden
van Python 2 op te lossen. Voor studenten voor wie programmeren nieuw
is, is dit een groot voordeel, omdat er minder "vreemde" taalelementen
zijn die ze moeten leren als ze Python 3 verkiezen boven Python 2.

Om een voorbeeld te geven, als je $$7/4$$ uitrekent in Python 2, krijg je
als antwoord $$1$$, en niet $$1.75$$ wat je zou verwachten. De reden is dat
zowel $$7$$ als $$4$$ gehele getallen zijn ("integers"), en daarom is de
uitkomst van de deling ook een geheel getal. Als je $$1.75$$ als uitkomst
wilt hebben, moet je ervoor zorgen dat minstens een van de twee getallen
een gebroken getal is. $$7.0/4$$ geeft daarom als uitkomst $$1.75$$. Dit is
de manier waarop vrijwel alle computertalen omgaan met getallen. Voor
studenten voor wie programmeren nieuw is, is dit contra-intuïtief.
Python 3 heeft dit probleem opgelost, en doet de conversie naar gebroken
getallen automatisch. Dus in Python 3 geeft $$7/4$$ de uitkomst $$1.75$$.
Veel Python 2 programma's zijn echter geschreven onder de aanname dat
een integer-deling naar beneden afrondt, wat betekent dat deze
programma's niet meer correct functioneren als je ze uitvoert als Python
3 programma's. Dus zijn Python 2 en Python 3 niet compatibel.

Omdat Python 3 intuïtiever is dan Python 2, en omdat vandaag de dag de
meeste Python programma's en modules op zijn minst geconverteerd zijn
naar Python 3, is dit boek geschreven voor Python 3. Als je ooit terug
moet naar Python 2, is dat niet moeilijk. De verschillen tussen Python 2
en Python 3 die ik ken heb ik beschreven in appendix
30
(dit is geen compleet overzicht). Als je alleen Python 3 wilt gebruiken,
kun je die appendix laten voor wat het is. Maar omdat ik vaak de vraag
"wat zijn precies de verschillen tussen Python 2 en Python 3" gesteld
krijg, leek het me verstandig deze appendix op te nemen.
