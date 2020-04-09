from random import randint

NUMKRUIPERS = 1000000000
num = NUMKRUIPERS
dood = int( num / 3 )
if NUMKRUIPERS % 3:
    if randint( 0, NUMKRUIPERS % 3 ): # Kruiper over op dag 1
        dood += 1
leeftijd = dood # Dag-1 doden leven 1 dag
num -= dood

dag = 2
while num > 0:
    dood = int( num / 2 )
    num -= dood # Dood de helft
    if dood != num: # Er is er 1 over
        if randint( 0, 1 ): # Besluit of 1 sterft
            dood, num = num, dood # Verwissel waardes
    leeftijd += dood * dag
    dag += 1

print( "{:.2f}".format( leeftijd / NUMKRUIPERS ) )
