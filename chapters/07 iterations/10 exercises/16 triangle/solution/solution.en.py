from random import randint

NUMCRAWLERS = 100000
totalage = NUMCRAWLERS # They all live at least one day

for i in range( NUMCRAWLERS ):
    if randint( 0, 2 ): # Don't die on first day
        totalage += 1
        while randint( 0, 1 ): # Don't die on following day
            totalage += 1

print( "{:.2f}".format( totalage / NUMCRAWLERS ) )
