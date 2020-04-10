In de code hieronder heb ik een recursieve
implementatie gedaan van het vragen aan de gebruiker om een string,
waarin alleen kleine letters mogen worden gebruikt. Als de gebruiker
iets ingeeft waar een incorrect teken in zit, zorgt een recursieve
aanroep naar de functie ervoor dat een nieuwe input gevraagd wordt. Dit
lijkt erop dat de loop-en-een-half vermeden wordt. 

### Opgave

Hoewel het altijd een
slechte zaak is om de diepte van een recursieve aanroep afhankelijk te
maken van de gebruiker, is deze implementatie niet alleen slecht, maar
zelfs behoorlijk fout. Zie je wat er fout aan is, en hoe dat veroorzaakt
wordt?

{:class="callout callout-info"}
> #### Tip
> Het is niet de expressie `letter < 'a' or letter > 'z'`; die vergelijkingen zijn in orde.

{:class="callout callout-info"}
> #### Opmerking
> Ik wil met klem benadrukken dat het idee hieronder slecht is. Je moet geen recursie gebruiken om doorsnee problemen af te handelen die net zo goed met iteraties gedaan kunnen worden. Recursie is bedoeld voor uitzonderlijke situaties. Zie dit niet als een voorbeeld van recursie, maar zie het als een voorbeeld van hoe recursie *niet* gebruikt moet worden. De voornaamste reden dat ik de code hier opneem is dat ik soms zie dat studenten dit soort code schrijven, en ik wil expliciet maken dat dat een slecht idee is.
