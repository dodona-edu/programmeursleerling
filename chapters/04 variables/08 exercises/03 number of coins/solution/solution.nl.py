# bedrag (in cent)
bedrag = 1156

# waarde van munstukken vastleggen
centen_in_dollar = 100
centen_in_kwartje = 25
centen_in_dubbeltje = 10
centen_in_stuiver = 5

# minimaal aantal muntstukken bepalen
dollars = bedrag // centen_in_dollar
centen = bedrag % centen_in_dollar

kwartjes = centen // centen_in_kwartje
centen = centen % centen_in_kwartje

dubbeltjes = centen // centen_in_dubbeltje
centen = centen % centen_in_dubbeltje

stuivers = centen // centen_in_stuiver
centen = centen % centen_in_stuiver

# minimaal aantal muntstukken uitschrijven
print(f'Dollars: {dollars}')
print(f'Kwartjes: {kwartjes}')
print(f'Dubbeltjes: {dubbeltjes}')
print(f'Stuivers: {stuivers}')
print(f'Centen: {centen}')
