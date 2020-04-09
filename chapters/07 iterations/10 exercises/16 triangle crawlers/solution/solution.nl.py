from random import randint

NUMKRUIPERS = 100000
leeftijd = NUMKRUIPERS # Ze leven minstens een dag

for i in range( NUMKRUIPERS ):
    if randint( 0, 2 ): # Sterf niet op dag 1
        leeftijd += 1
        while randint( 0, 1 ): # Sterf niet
            leeftijd += 1

print( "{:.2f}".format( leeftijd / NUMKRUIPERS ) )
